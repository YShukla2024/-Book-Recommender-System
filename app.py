import streamlit as st
import pandas as pd
import pickle
import numpy as np
import requests
from PIL import Image, ImageDraw, ImageFont
import io
from functools import lru_cache
import random

# Load preprocessed data and models
@st.cache_resource
def load_data():
    try:
        return {
            'popular_df': pickle.load(open('model/popular.pkl', 'rb')),
            'pt': pickle.load(open('model/pt.pkl', 'rb')),
            'books': pickle.load(open('model/books.pkl', 'rb')),
            'similarity_scores': pickle.load(open('model/similarity_scores.pkl', 'rb'))
        }
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.stop()

data = load_data()
popular_df = data['popular_df']
pt = data['pt']
books = data['books']
similarity_scores = data['similarity_scores']

# Enhanced book cover fetcher with multiple fallback options
@lru_cache(maxsize=1000)
def fetch_book_cover(title, author, isbn=None, fallback_url=None):
    """
    Try multiple sources to get book cover with better error handling
    Returns a PIL Image object
    """
    # Clean inputs
    clean_title = ''.join(c for c in str(title) if c.isalnum() or c in " -_").strip()
    clean_author = ''.join(c for c in str(author) if c.isalnum() or c in " -_").strip()
    clean_isbn = ''.join(c for c in str(isbn) if c.isdigit()) if isbn else None
    
    # Try Open Library first with ISBN
    if clean_isbn:
        try:
            url = f"https://covers.openlibrary.org/b/isbn/{clean_isbn}-L.jpg"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return Image.open(io.BytesIO(response.content))
        except:
            pass

    # Try Google Books API with title+author
    try:
        query = f"intitle:{clean_title}+inauthor:{clean_author}"
        google_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
        response = requests.get(google_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('items'):
                image_url = data['items'][0]['volumeInfo'].get('imageLinks', {}).get('thumbnail', '')
                if image_url:
                    image_url = image_url.replace("http://", "https://").replace("zoom=1", "zoom=2")
                    img_response = requests.get(image_url, timeout=10)
                    if img_response.status_code == 200:
                        return Image.open(io.BytesIO(img_response.content))
    except:
        pass

    # Try the provided fallback URL
    if fallback_url:
        try:
            fallback_url = fallback_url.replace("http://", "https://")
            response = requests.get(fallback_url, timeout=10)
            if response.status_code == 200:
                return Image.open(io.BytesIO(response.content))
        except:
            pass

    # Final fallback - generate an informative placeholder
    return generate_placeholder(title, author)

def generate_placeholder(title, author):
    """Generate a placeholder image with book info"""
    img = Image.new('RGB', (200, 300), color=(240, 240, 240))
    try:
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 14)
        except:
            font = ImageFont.load_default()
        
        # Add title (split into multiple lines if needed)
        title_lines = []
        words = str(title).split()
        current_line = ""
        for word in words:
            if len(current_line + word) <= 20:
                current_line += f"{word} "
            else:
                title_lines.append(current_line.strip())
                current_line = f"{word} "
        if current_line:
            title_lines.append(current_line.strip())
        
        # Draw title lines
        y_position = 50
        for line in title_lines[:3]:  # Max 3 lines
            draw.text((100, y_position), line, font=font, fill="black", anchor="mm")
            y_position += 25
        
        # Add author
        author_text = f"by {author}" if author else ""
        draw.text((100, 200), author_text, font=font, fill="darkblue", anchor="mm")
        
        # Add "Cover Not Available" text
        draw.text((100, 250), "Cover Not Available", font=font, fill="gray", anchor="mm")
        
        # Add decorative border
        draw.rectangle([5, 5, 195, 295], outline="lightgray", width=2)
    except:
        pass
    return img

# Function to display a book card
def display_book(col, book_info, similarity=None):
    with col:
        # Get book details
        title = book_info['Book-Title']
        author = book_info['Book-Author']
        isbn = book_info.get('ISBN', '')
        img_url = book_info.get('Image-URL-M', '')
        
        # Fetch or generate cover
        cover_img = fetch_book_cover(title, author, isbn, img_url)
        
        # Display the image
        col.image(cover_img, width=150, use_container_width=True)
        
        # Display book info
        col.markdown(f"**{title}**")
        col.caption(f"by {author}")
        
        if similarity is not None:
            col.progress(float(similarity))
            col.caption(f"Similarity: {similarity:.0%}")
        else:
            rating_fields = ['Avg_rating', 'avg_rating', 'Avg_ratings']
            rating = next((book_info[field] for field in rating_fields if field in book_info), 0)
            col.caption(f"Rating: {float(rating):.1f} ★ ({book_info.get('num_ratings', 0)} reviews)")

# Page config
st.set_page_config(
    page_title="Book Recommender System",
    page_icon="📚",
    layout="wide"
)

# Sidebar
st.sidebar.title("Filters")
selected_type = st.sidebar.radio(
    "Recommendation Type",
    ["Popular Books", "Personalized Recommendations"]
)

# Main content
st.title("📚 Book Recommender System")

if selected_type == "Popular Books":
    st.header("Top 50 Popular Books")
    
    # Display books in rows of 5
    cols_per_row = 5
    for i in range(0, len(popular_df), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(popular_df):
                display_book(cols[j], popular_df.iloc[i + j])

else:
    st.header("Personalized Recommendations")
    book_name = st.selectbox(
        "Select a book you like:",
        pt.index.values
    )
    
    if st.button("Recommend Similar Books"):
        with st.spinner('Finding similar books...'):
            try:
                idx = np.where(pt.index == book_name)[0][0]
                similar_items = sorted(
                    list(enumerate(similarity_scores[idx])),
                    key=lambda x: x[1],
                    reverse=True
                )[1:6]  # Top 5 similar books
                
                cols = st.columns(5)
                for i, (index, score) in enumerate(similar_items):
                    book_info = books[books['Book-Title'] == pt.index[index]].iloc[0]
                    display_book(cols[i], book_info, score)
            except Exception as e:
                st.error(f"Error generating recommendations: {str(e)}")
                st.error("Please try another book or check your connection.")

# Footer
st.markdown("---")
st.caption("Yash Shukla")
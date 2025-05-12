# 📚 Book Recommendation System


📝 Project Overview

This project is a Book Recommendation System built using Python and Streamlit. It recommends books based on user selection or popularity using collaborative filtering techniques. The app also fetches book covers from public APIs to enrich the UI experience.

⚙️ Tech Stack

Frontend: Streamlit

Backend/Data Handling: Python (pandas, NumPy,Scikit-learn,jupyter-notebook)

Storage: Pickle files (.pkl) for fast loading

APIs Used: Open Library API, Google Books API

📂 Folder Structure

📁 Book-Recommender-System/
│
├── 📁 dataset/                      # Raw dataset files
│   ├── Books.csv                   # Book metadata
│   ├── Ratings.csv                 # User-book ratings
│   └── Users.csv                   # User demographic info
│
├── 📁 image/                        # (Unused or placeholder for static images)
│
├── 📁 model/                        # Preprocessed data and models
│   ├── books.pkl                   # Book metadata (processed)
│   ├── popular.pkl                 # Top 50 popular books
│   ├── pt.pkl                      # Pivot table (user vs. book matrix)
│   └── similarity_scores.pkl       # Cosine similarity matrix
│
├── app.py                          # Main Streamlit app
├── book-recommender-system.ipynb  # Notebook for development/experiments
├── requirement.txt                 # Dependencies list (for pip install)

🔍 Features

1. Popular Books

Displays top 50 books by average rating & review count.

Each book includes: title, author, cover image, rating, and review count.

2. Personalized Recommendations

User selects a book they like.

Recommends top 5 similar books based on cosine similarity of user-book matrix.

3. Book Cover Handling

Tries ISBN via Open Library first.

Falls back to Google Books API (title+author).

If all fail, generates a placeholder using PIL.

🧰 Recommendation Logic

Based on Collaborative Filtering.

A user-book rating pivot table (pt.pkl) is created.

Cosine similarity is precomputed and stored in similarity_scores.pkl.

🚀 How to Run

Clone the repository:

git clone [(https://github.com/YShukla2024/-Book-Recommender-System)]
cd book-recommender-system

Install dependencies:

pip install -r requirement.txt

Run the Streamlit app:

streamlit run app.py

⚠️ Warnings

missing ScriptRunContext: This is a Streamlit internal warning. Can be safely ignored.

👤 Author

Name: Yash Shukla

Email: shuklayash125@gmail.com

GitHub: github.com/YShukla2024

🔧 Future Improvements

Add user login system

Enable user-based collaborative filtering

Store and retrieve personalized history

Responsive UI enhancements

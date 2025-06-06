# 📚 Book Recommendation System

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://xauwsbqco9c9h78tenxv4p.streamlit.app/)

---

## 📝 Overview

Welcome to the **Book Recommendation System**!  
This interactive web app suggests books you’ll love, based on your previous choices and popular trends. Whether you’re an avid reader or looking for your next favorite novel, this app helps you discover great books, complete with cover images and ratings.

---

## ⚙️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend/Data Handling:** Python (`pandas`, `NumPy`, `scikit-learn`, `jupyter-notebook`)
- **Storage:** Pickle files (`.pkl`) for lightning-fast data loading
- **APIs:** [Open Library API](https://openlibrary.org/developers/api), [Google Books API](https://developers.google.com/books)

---

## 📂 Project Structure

```
Book-Recommender-System/
│
├── dataset/                  # 📊 Raw data files
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│
├── image/                    # 🖼️ (Placeholder for static images)
│
├── model/                    # 🤖 Preprocessed data & models
│   ├── books.pkl
│   ├── popular.pkl
│   ├── pt.pkl
│   └── similarity_scores.pkl
│
├── app.py                    # 🚀 Main Streamlit app
├── book-recommender-system.ipynb  # 🧪 Jupyter notebook for development
├── requirement.txt           # 📦 Dependencies list
```

---

## ✨ Features

### 🌟 1. **Popular Books**
- View the top 50 books ranked by ratings & review counts.
- Each entry shows: **title, author, cover image, rating, reviews**.

### 🎯 2. **Personalized Recommendations**
- Select a book you enjoy.
- Instantly get 5 similar book suggestions, powered by collaborative filtering and cosine similarity!

### 🖼️ 3. **Smart Book Covers**
- Fetches covers using ISBN from Open Library.
- Falls back to Google Books API (title & author) if needed.
- Still no cover? A custom placeholder image is generated with [PIL](https://pillow.readthedocs.io/).

---

## 🧠 How Recommendations Work

- **Collaborative Filtering:**  
  Utilizes a user-book rating pivot table (`pt.pkl`) and precomputed cosine similarities (`similarity_scores.pkl`).
- **Workflow:**  
  1. User selects a book  
  2. System finds similar books based on what other users like  
  3. Recommendations appear instantly

---

## 🚀 Quick Start

**1. Clone the repository:**
```bash
git clone <repo-url>
cd book-recommender-system
```

**2. Install dependencies:**
```bash
pip install -r requirement.txt
```

**3. Launch the app:**
```bash
streamlit run app.py
```
> _Tip: Ignore the `missing ScriptRunContext` warning from Streamlit—it’s harmless!_

---

## 👤 Author

- **Name:** Yash Shukla  
- **Email:** shuklayash125@gmail.com  
- **GitHub:** [YShukla2024](https://github.com/YShukla2024)

---

## 🔮 What’s Next?

- 🔐 User login & personalized profiles
- 👥 User-based collaborative filtering
- 🕒 Save & retrieve personalized history
- 📱 Responsive UI for mobile/tablet

---

## 🙏 Acknowledgements

- [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)  
- [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Scikit-Learn](https://scikit-learn.org/), [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- [Kaggle](https://www.kaggle.com/) & the open-source community 🌍

---
> *“The only thing that you absolutely have to know, is the location of the library.”* — _Albert Einstein_

---

_Discover your next favorite book now!_ 📖✨

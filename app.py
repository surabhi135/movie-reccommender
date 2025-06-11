import streamlit as st
import pickle
import pandas as pd
import streamlit as st
import base64

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
def set_text_color():
    st.markdown(
        """
        <style>
        .stApp {
            color: white; /* Change to black, grey, or white depending on background */
        }

        h1, h2, h3, h4, h5, h6, p {
            color: white;
        }

        .css-1v0mbdj { color: white; } /* dropdown text */
        .css-10trblm { color: white; } /* titles and headers */
        </style>
        """,
        unsafe_allow_html=True
    )
def style_button():
    st.markdown(
        """
        <style>
        div.stButton > button {
            color: white;                     /* Button text color */
            background-color: #ff4b4b;       /* Button background */
            border-radius: 12px;
            padding: 0.5em 2em;
            font-weight: bold;
            border: none;
        }

        div.stButton > button:hover {
            background-color: #ff1c1c;       /* Hover color */
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Load your movie data and similarity matrix (you should already have this)
movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

# Function to recommend
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

# Streamlit UI
st.title("🎬 Bappy Movie Recommender")
set_background("background.jpg")  # Replace with your image file name
set_text_color()
style_button()
selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    for i, title in enumerate(recommendations, 1):
        st.write(f"👉 {title}")

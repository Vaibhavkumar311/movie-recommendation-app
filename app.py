import pickle
import streamlit as st
import pandas as pd

# ------------ Recommend Function ------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# ------------ Load Data ------------
movie_dict = pickle.load(open(r'C:\Users\LENOVO\PycharmProjects\PythonProject\class movie project\.venv\movie_dict.pkl','rb'))
similarity = pickle.load(open(r'C:\Users\LENOVO\PycharmProjects\PythonProject\class movie project\.venv\similarity.pkl','rb'))

movies = pd.DataFrame(movie_dict)

# ------------ Streamlit UI ------------
st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    st.subheader("Top 5 Recommended Movies:")

    # Horizontal card-style layout
    cols = st.columns(len(recommendations))  # 5 columns

    for idx, movie in enumerate(recommendations):
        with cols[idx]:
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #4CAF50;
                    border-radius: 12px;
                    padding: 20px;
                    text-align: center;
                    background-color: #f0f0f0;
                    font-weight: bold;
                    font-size: 16px;
                    box-shadow: 2px 2px 8px #aaa;
                    transition: transform 0.2s, background-color 0.2s;
                    cursor: pointer;
                " onmouseover="this.style.backgroundColor='#d4ffd4'; this.style.transform='scale(1.05)';"
                   onmouseout="this.style.backgroundColor='#f0f0f0'; this.style.transform='scale(1)';"
                >
                    🎥 {movie}
                </div>
                """,
                unsafe_allow_html=True
            )



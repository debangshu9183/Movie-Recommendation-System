import streamlit as st
import pickle
import pandas as pd

# Load movie data
st.title('Movie Recommendation System')

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity_file.pkl', 'rb'))  # Ensure correct filename

# Movie selection dropdown
selected_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values
)

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)  # Use movies DataFrame
    return recommended_movies

# Button to show recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    st.write("Top 5 Recommended Movies:")
    for movie in recommendations:
        st.write(movie)  # Display in Streamlit

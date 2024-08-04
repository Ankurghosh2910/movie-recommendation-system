import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]  # Get top 10 recommendations

    recommend_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movies_poster

# Load the data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Create columns for horizontal display
    cols = st.columns(5)  # Adjust based on your screen size; 5 columns in a row

    # Display the first 5 recommendations in the first row
    for col, name, poster in zip(cols, names[:5], posters[:5]):
        with col:
            st.image(poster, caption=name)

    # Create columns for the next 5 recommendations
    cols = st.columns(5)

    # Display the next 5 recommendations in the second row
    for col, name, poster in zip(cols, names[5:], posters[5:]):
        with col:
            st.image(poster, caption=name)

# Movie Recommendation System

## Overview

This project is a Movie Recommendation System built using Python, Streamlit, and machine learning techniques. It provides personalized movie recommendations based on user input. The system uses a similarity matrix to suggest movies similar to the one selected by the user.

## Features

- **Movie Recommendations**: Get a list of movie recommendations based on the selected movie.
- **Movie Posters**: View posters of the recommended movies.
- **Interactive UI**: Built with Streamlit for a user-friendly experience.

## Deployment

The application is deployed on Streamlit and can be accessed via the following link:

[Movie Recommendation System](https://movie-recommendation-system-kxfjrynfxrmq5browdow4p.streamlit.app/)

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Ankurghosh2910/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Requests
- Pickle

## Data Files

- `movie_dict.pkl`: Contains movie data used for recommendations.
- `similarity.pkl`: Contains the similarity matrix for movie recommendations.

## Usage

1. Select a movie from the dropdown menu.
2. Click the "Recommend" button to view recommendations.
3. The app will display a list of recommended movies along with their posters.

## Contributing

A special thanks to [Tanmay Kule]([https://github.com/tanmaykule](https://github.com/oblionC)) for his valuable assistance in this project.

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are highly appreciated!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/) for the easy-to-use interface.
- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) for movie data.

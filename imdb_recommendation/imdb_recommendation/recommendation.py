import imdb

# Function to get the top-rated movies from IMDb
def get_top_rated_movies():
    # Create an IMDb object
    ia = imdb.IMDb()
    
    # Retrieve the top 250 movies
    top_movies = ia.get_top250_movies()
    
    return top_movies

# Function to recommend movies based on a given movie title
def recommend_movie(movie_title):
    # Create an IMDb object
    ia = imdb.IMDb()
    
    # Search for the movie based on the provided title
    search_results = ia.search_movie(movie_title)
    
    # If no search results are found, return None
    if not search_results:
        return None

    # Get the first movie from the search results
    movie = search_results[0]
    
    # Update the movie details
    ia.update(movie)

    # Extract the genre of the movie
    genre = movie.get('genres', [])

    # Get movies with the same genre as the searched movie
    recommended_movies = ia.get_movies(genre=genre)

    # Return the top 5 recommended movies
    return recommended_movies[:5]

# Replace "Movie Title" with the title of the movie you want recommendations for
recommendations = recommend_movie("Movie Title")

# Print the recommendations
print(recommendations)

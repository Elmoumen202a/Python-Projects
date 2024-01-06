# Import the IMDb class from IMDbPY library
from imdb import IMDb

# Define a function to get the top 250 movies from IMDb
def get_top250_movies():
    # Create an instance of the IMDb class
    imdb_instance = IMDb() 
    # Get the top 250 movies
    movies = imdb_instance.get_top250_movies()  
    # Return the list of top 250 movies
    return movies

# Define a function to print the top 250 movies
def print_top250_movies():
    # Get the top 250 movies using the previously defined function
    movies = get_top250_movies()  
    # Print each movie in the list
    for i in movies:
        print(i)
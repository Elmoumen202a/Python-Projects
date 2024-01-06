from scrapeIMDb import get_top250_movies

# Define a test function for get_top250_movies
def test_get_top250_movies():
    # Call the function to get the top 250 movies
    movies = get_top250_movies()
    
    # Assert that the result is a list
    assert isinstance(movies, list)
    
    # Assert that the list contains exactly 250 movies
    assert len(movies) == 250
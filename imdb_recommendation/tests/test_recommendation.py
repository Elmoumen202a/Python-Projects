from imdb_recommendation.recommendation import get_top_rated_movies, recommend_movie

# Test function for get_top_rated_movies
def test_get_top_rated_movies():
    # Get the top-rated movies
    top_movies = get_top_rated_movies()

    # Assert that the number of top movies is 250
    assert len(top_movies) == 250

# Test function for recommend_movie
def test_recommend_movie():
    # Get movie recommendations for the movie "Inception"
    recommendations = recommend_movie("Inception")

    # Assert that recommendations are not None
    assert recommendations is not None

    # Assert that there are 5 recommended movies
    assert len(recommendations) == 5

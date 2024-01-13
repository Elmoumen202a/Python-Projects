import pytest
import scraper

@pytest.fixture
def app():
    return scraper.app

@pytest.fixture
def test_client(app):
    return app.test_client()

def test_scrape_route(test_client):
    # Send a GET request to the /scrape route
    response = test_client.get('/scrape')

    # Check if the response status is 200 OK
    assert response.status == "200 OK"

    # You may add more specific assertions based on the expected content
    assert b"Example Domain" in response.data

if __name__ == "__main__":
    pytest.main([__file__])
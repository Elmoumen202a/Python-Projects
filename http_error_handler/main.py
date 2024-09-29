import requests

# Custom exception for handling HTTP errors
class HTTPError(Exception):
    pass

# Function to handle HTTP errors based on status codes
def handle_http_error(status_code):
    """
    This function takes an HTTP status code as input and raises an HTTPError
    with a custom message based on the status code. It handles common errors
    like 400, 401, 403, 404, and 500.
    """
    if status_code == 400:
        raise HTTPError("400 Bad Request")
    elif status_code == 401:
        raise HTTPError("401 Unauthorized")
    elif status_code == 403:
        raise HTTPError("403 Forbidden")
    elif status_code == 404:
        raise HTTPError("404 Not Found")
    elif status_code == 500:
        raise HTTPError("500 Internal Server Error")
    else:
        # For unhandled status codes, just print the code
        print(f"Status code {status_code} is not handled")

# Function to make a GET request and check for errors
def make_request(url):
    """
    This function sends a GET request to the provided URL and checks the response
    for HTTP errors. If an error is found, it calls the handle_http_error() function.
    """
    try:
        # Sending the GET request to the URL
        response = requests.get(url)

        # Checking the response status code and handling errors
        handle_http_error(response.status_code)
        print("Request was successful")  # If no error, request was successful
    except HTTPError as e:
        # If an HTTPError is raised, print the error message
        print(f"Error occurred: {e}")

# Main block to simulate an HTTP request
if __name__ == "__main__":
    # Simulating a 404 Not Found error by sending a request to an invalid URL
    url = "https://httpstat.us/404"
    make_request(url)

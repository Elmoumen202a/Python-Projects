import requests

def is_url_valid(url):
    """
    Checks if a URL is valid.
    
    Parameters:
    url (str): The URL to check
    
    Returns:
    bool: True if the URL is valid, False otherwise
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    if is_url_valid(url):
        print(f"The URL '{url}' is valid.")
    else:
        print(f"The URL '{url}' is not valid.")
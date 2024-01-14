import requests
from bs4 import BeautifulSoup as bs

def get_github_profile_picture(github_profile):
    """
    Get the profile picture of a GitHub user.

    Parameters:
    github_profile (str): The GitHub profile URL.
    Returns: str ,the URL of the user's profile picture.
    """
    req = requests.get(github_profile)
    scraper = bs(req.content, "html.parser")
    
    # Find the profile picture URL
    profile_picture_element = scraper.find("img", class_="avatar-user")
    
    if profile_picture_element:
        profile_picture_url = profile_picture_element["src"]
        return profile_picture_url
    else:
        return None

# Example usage:
github_profile_url = "https://github.com/Elmoumen202a"
profile_picture_url = get_github_profile_picture(github_profile_url)
print("Profile Picture URL:", profile_picture_url)

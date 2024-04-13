import hashlib

class URLShortener:
    def __init__(self):
        # Initialize an empty dictionary to store the mapping of shortened URLs to original URLs
        self.url_mapping = {}

    def shorten_url(self, url):
        """
        Shortens a given URL by generating a unique hash.
        Args:
            url (str): The original URL to be shortened.
        Returns:
            str: The shortened URL.
        """
        # Generate a unique hash for the URL using SHA-256 algorithm
        url_hash = hashlib.sha256(url.encode()).hexdigest()[:8]
        # Store the mapping of the shortened URL to the original URL
        self.url_mapping[url_hash] = url
        return url_hash

    def get_original_url(self, short_url):
        """
        Retrieves the original URL from the shortened URL.
        Args:
            short_url (str): The shortened URL.
        Returns:
            str: The original URL if found, otherwise None.
        """
        return self.url_mapping.get(short_url, None)

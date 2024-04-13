# URL Shortener

A simple URL Shortener implemented in Python.

## How to Use

1. Import `URLShortener` from `main.py`.
2. Create an instance of `URLShortener`.
3. Use the `shorten_url` method to shorten a URL.
4. Use the `get_original_url` method to retrieve the original URL.

## Example

```python
from main import URLShortener

shortener = URLShortener()
original_url = "https://www.example.com"
short_url = shortener.shorten_url(original_url)
print("Shortened URL:", short_url)
retrieved_url = shortener.get_original_url(short_url)
print("Original URL:", retrieved_url)

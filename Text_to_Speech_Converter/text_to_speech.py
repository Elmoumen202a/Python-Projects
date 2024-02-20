import nltk
from newspaper import Article
from gtts import gTTS

def text_to_speech(url):
    # Create an Article object and download/parse the content from the given URL
    article = Article(url)
    article.download()
    article.parse()
    
    # Download the NLTK 'punkt' tokenizer if not already downloaded
    nltk.download('punkt')
    
    # Apply natural language processing to the article
    article.nlp()
    
    # Extract the text content of the article
    article_text = article.text
    
    # Set the language for text-to-speech conversion
    language = 'en'
    
    # Create a gTTS object with the article text and save it as an MP3 file
    my_obj = gTTS(text=article_text, lang=language, slow=False)
    my_obj.save("read_article.mp3")

if __name__ == '__main__':
    # Get the URL input from the user
    user_url = input("Enter the URL of the article you want to convert to speech: ")
    
    try:
        # Call the text_to_speech function with the user-provided URL
        text_to_speech(url=user_url)
        print("Text-to-speech conversion completed. Check the 'read_article.mp3' file.")
    except Exception as e:
        # Handle any exceptions that may occur during the conversion process
        print(f"An error occurred: {e}")

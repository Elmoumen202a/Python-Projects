from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unknown"

if __name__ == "__main__":
    text = input("Enter text: ")
    language = detect_language(text)
    print("Detected language:", language)

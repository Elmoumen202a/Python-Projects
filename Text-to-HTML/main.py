def text_to_html(text):
    # Convert text to HTML here
    return f"<p>{text}</p>"

if __name__ == "__main__":
    input_text = input("Enter your text: ")
    html_output = text_to_html(input_text)
    print(html_output)

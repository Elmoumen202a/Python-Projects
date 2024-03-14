import PyPDF2

def extract_text_from_pdf(pdf_file):
    """Extract text content from the PDF file."""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
        return text

def search_text_in_pdf(pdf_text, query):
    """Search for the query text in the extracted PDF content."""
    # Perform search in the PDF text
    # You can implement more sophisticated search logic here
    if query in pdf_text:
        return "Found"
    else:
        return "Not found"

if __name__ == "__main__":
    pdf_file = 'sample.pdf'  # Change this to your PDF file name
    pdf_text = extract_text_from_pdf(pdf_file)

    query = input("Enter your query: ")
    result = search_text_in_pdf(pdf_text, query)
    print(result)

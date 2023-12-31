import PyPDF2

def extract_text_from_pdf(pdf_file):
    try:
        with open(pdf_file, "rb") as pdf:
            reader = PyPDF2.PdfFileReader(pdf)
            page = reader.getPage(0)
            text = page.extractText()
            return text
    except Exception as e:
        return f"Error: {e}"

def main():
    pdf_file_name = input("Enter the name of the PDF file (including extension): ")
    extracted_text = extract_text_from_pdf(pdf_file_name)
    
    if "Error" in extracted_text:
        print(extracted_text)
    else:
        print("Text extracted from the PDF:")
        print(extracted_text)

if __name__ == "__main__":
    main()

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_business_card(name, title, company, email, phone):
    pdf_filename = "business_card.pdf"

    # Create a PDF document
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a list to hold the content
    content = []

    # Add business card details as Paragraphs
    content.append(Paragraph(f"<b>Name:</b> {name}", styles['Normal']))
    content.append(Paragraph(f"<b>Title:</b> {title}", styles['Normal']))
    content.append(Paragraph(f"<b>Company:</b> {company}", styles['Normal']))
    content.append(Paragraph(f"<b>Email:</b> {email}", styles['Normal']))
    content.append(Paragraph(f"<b>Phone:</b> {phone}", styles['Normal']))

    # Build the PDF document
    doc.build(content)

    print(f"Business card generated and saved as {pdf_filename}")

if __name__ == "__main__":
    # Get user input for business card details
    name = input("Enter your name: ")
    title = input("Enter your title: ")
    company = input("Enter your company: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    # Generate and print the business card
    generate_business_card(name, title, company, email, phone)

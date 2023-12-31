import os
import pytest
from extract import extract_text_from_pdf

@pytest.fixture
def pdf_file_path(tmpdir):
    # Create a temporary PDF file for testing
    pdf_content = "Test PDF content."
    pdf_file_path = os.path.join(tmpdir, "test.pdf")
    with open(pdf_file_path, "w") as pdf_file:
        pdf_file.write(pdf_content)
    return pdf_file_path

def test_extract_text_from_pdf(pdf_file_path):
    # Test the extract_text_from_pdf function
    extracted_text = extract_text_from_pdf(pdf_file_path)
    assert "Test PDF content" in extracted_text

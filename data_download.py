import fitz  # PyMuPDF
import requests
import os

def download_pdf(url):
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    # Save the PDF temporarily
    temp_pdf_path = "temp_pdf_file.pdf"
    with open(temp_pdf_path, 'wb') as f:
        f.write(response.content)
    
    return temp_pdf_path
def pdf_to_text(pdf_path):
    # Open the downloaded PDF file
    document = fitz.open(pdf_path)
    text_content = ''
    # Extract text from each page
    for page in document:
        text_content += page.get_text()
    # Close the document
    document.close()
    
    # Optionally, remove the temporary file after processing
    os.remove(pdf_path)
    return text_content
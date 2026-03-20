from pypdf import PdfReader

def pdf_reader(filename):
    reader = PdfReader(filename)
    text =""
    for pages in reader.pages:
        text+=pages.extract_text()

    return text

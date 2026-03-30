from pypdf import PdfReader

def pdf_reader(filename):
    reader = PdfReader(filename)
    pages = []
    for page in  reader.pages:
        pages.append(page.extract_text())
    return pages                                        
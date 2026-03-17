from pdf_loader import pdf_reader
from text_processing import chunk_text


def main():
    text = pdf_reader("filename.pdf")
    process = chunk_text(text=text, chunk_size=500)
    print(process)
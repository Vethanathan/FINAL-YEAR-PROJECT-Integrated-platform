from PyPDF2 import PdfReader
def pdf_to_txt(pdf_file,file_name):
    reader = PdfReader(pdf_file)
    # number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    with open(file_name ,"w") as f1:
        f1.write(text)
    return "DONE"
    
# importing required modules
from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PdfReader("2.pdf")

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
for i in range(len(reader.pages)):
    page = reader.pages[i]

    # extracting text from page
    text = page.extract_text()
    print(text)


# import os
# import PyPDF2 
# os.chdir("C:\\Users\\piyush kumar\\Downloads")
# a = os.listdir("C:\\Users\\piyush kumar\\Downloads")

# b=[file for file in a if file.endswith(".pdf")]
# first = True
# for pdf in b :
#      if first :
#          pdf_pathfile = os.path.join("C:\\Users\\piyush kumar\\Downloads", pdf)
#          with open(pdf_pathfile, 'rb') as pdf_file:
#           pdf_reader = PyPDF2.PdfReader(pdf_file)
#           page=pdf_reader.pages(0)
#           print(page.extractText())
# first=False  



import os
import PyPDF2

os.chdir("C:\\Users\\piyush kumar\\Downloads")
a = os.listdir("C:\\Users\\piyush kumar\\Downloads")

# Filter PDF files
pdf_files = [file for file in a if file.endswith(".pdf")]

first = True
for pdf_file in pdf_files:
    if first:
        pdf_pathfile = os.path.join("C:\\Users\\piyush kumar\\Downloads", pdf_file)
        with open(pdf_pathfile, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            page = pdf_reader.pages[0]  # Corrected the indexing here
            text = page.extract_text()  # Corrected the method name
            print(f"Text extracted from {pdf_file}:\n{text}")
        first = False

from PyPDF2 import PdfWriter, PdfReader
import pandas as pd

inputpdf = PdfReader(open("IT-Day_Certificates.pdf", "rb"))

db = pd.read_excel("itsc_mail.xlsx")


for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open("op/%s IT Day Certificate.pdf" % db['Names'][i], "wb") as outputStream:
        output.write(outputStream)
#Install the dependancies.
import cv2
import pdf2image
import pytesseract
import os 
import PyPDF2
from PyPDF2 import PdfFileWriter
def conversion(input,output):
    try:
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        TESSDATA_PREFIX='C:/Program Files/Tesseract-OCR'
        tessdata_dir_config='--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
        img=cv2.imread(input,1)
        result=pytesseract.image_to_pdf_or_hocr(img,lang="eng",config=tessdata_dir_config)
        f=open(output,"wb")
        f.write(bytearray(result))
        f.close()
    except:
        pass
def pdftoimagetopdf(input,foutput):
    try:
        os.mkdir('C:/pdftopdf')
    except:
        pass
    output='C:/pdftopdf/'
    i=0
    pil_images=pdf2image.convert_from_path(input,output_folder=None,first_page=None,last_page=None,fmt='jpg',userpw=None,use_cropbox=False,strict=False,poppler_path='C:/Program Files/poppler-0.68.0/bin')
    for image in pil_images:
        image.save(''+output+''+str(i)+'.jpg')
        i=i+1
    for j in range(0,i):
        conversion(''+output+''+str(j)+'.jpg',''+output+'s'+str(j)+'.pdf')
    pdf_writer = PdfFileWriter()
    for k in range(0,i):
        pdfFileObj = open(''+output+'s'+str(k)+'.pdf','rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(pdfReader.getNumPages()):
            pageObj = pdfReader.getPage(pageNum)
            pdf_writer.addPage(pageObj)
    pdfOutput = open(foutput,'wb')
    pdf_writer.write(pdfOutput)
    pdfOutput.close()
#Place the paths along with the file names here.
pdftoimagetopdf("<input file with entire path>","<output new file with entire path>")
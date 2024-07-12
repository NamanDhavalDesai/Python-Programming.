import cv2
import pdf2image
import pytesseract
from difflib import SequenceMatcher
from PIL import Image
from PIL import ImageFilter

try:
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    TESSDATA_PREFIX='C:/Program Files/Tesseract-OCR'
    tessdata_dir_config='--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
    img=cv2.imread('2.jpg',1)
    result=pytesseract.image_to_string(img,lang="eng",config=tessdata_dir_config)
except:
    print('a')
print(result)





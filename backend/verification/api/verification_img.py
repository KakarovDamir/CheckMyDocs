import pytesseract
import cv2
# from PIL import Image

import re

from re_patterns import *

def verify_img(filename, doctype:str='driver_license', filetype:str='img'):
    image = cv2.imread("filname")
    # image = Image.open("test.png")

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Zhkai\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    extracted = pytesseract.image_to_string(image, lang='rus')
    issue_date = re.findall(issue_date_pattern, extracted)
    doc_number = re.findall(doc_number_pattern, extracted)
    ssn = re.findall(ssn_pattern, extracted)


    print("issue date: ", issue_date[0].strip())
    print("doc number: ", doc_number[0].strip())
    print("ssn: ", ssn[0].strip())
import pytesseract
import cv2
# from PIL import Image

import re

from re_patterns import *

def verify_img(filename, doctype:str='driver_license'):
    if filename[-3:] == 'pdf':
        image = extract_img(filename)
    else:
        image = cv2.imread(filename)


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    cv2.imwrite('threshold_image.jpg', thresh1)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Zhkai\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    extracted = pytesseract.image_to_string(thresh1, lang='rus')
    print(extracted)

    license_number = re.findall(license_number_pattern, extracted)
    valid_date = re.findall(valid_date_pattern, extracted)

    print()
    print()
    print()
    print()

    print("license number: ", license_number[0].strip())
    print("valid date: ", valid_date[0][3:].strip())


def extract_img(filename):
    pass



def id_card(image):
    pass

def driver_license(image):
    pass


def sat(image):
    pass


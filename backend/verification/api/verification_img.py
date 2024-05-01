import os

import pytesseract
import cv2
from pypdf import PdfReader

import credentials


USERPROFILE = r'C:\Users\Zhkai'


def valid_doc(doctype: str, filename: str) -> bool:
    doc_types = ['driver_license', 'passport', 'id_card', 'sat']
    if doctype not in doc_types:
        return False
    elif filename[-4:] != '.jpg' or filename[-4:] != '.png' or filename[-5:] != '.jpeg':
        return False



def extract_from_pdf(filename):
    reader = PdfReader(filename)
    page = reader.pages[0]

    image_file_object = page.images[0].image
    with open(image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)

    image = cv2.imread(image_file_object.name)
    if image is None:
        print("error_extracting_image")

    os.remove(image_file_object.name)
    return image



def verify_img(filename: str, doctype: str='driver_license') -> tuple[bool, str | dict]:
    if not valid_doc(doctype, filename):
        return "wrong_format"
        
    if filename[-3:] == 'pdf':
        image = extract_from_pdf(filename)
    else:
        image = cv2.imread(filename)

    if image is None:
        return "wrong_format"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    # cv2.imwrite('threshold_image.jpg', thresh1)
    # os.remove('threshold_image.jpg')

    pytesseract.pytesseract.tesseract_cmd = rf'{USERPROFILE}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    extracted_text = pytesseract.image_to_string(thresh1, lang='rus')

    get_credentials = {
        'id_card': credentials.id_card,
        'driver_license': credentials.driver_license,
        'passport': credentials.passport,
        'sat': credentials.sat,
    }
    response, msg, ok = get_credentials[doctype](extracted_text)

    if not ok:
        return False, msg
    
    else:
        return True, response

    



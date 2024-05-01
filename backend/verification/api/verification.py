import os

import pytesseract
import cv2
from pypdf import PdfReader

from api import credentials
from api.check import check


USERPROFILE = r'C:\Users\Дамир'



def verify_document(file_type: str, filename: str, doctype: str = 'driver_license') -> tuple[bool, dict]:
    filename = rf'./media/{filename}'
    if file_type == 'pdf':
        print("verify pdf")
        is_valid, msg  = verify_from_pdf(filename, doctype)
    elif file_type == ".png" or file_type == ".jpg" or file_type == "image":
        print("verify image")
        is_valid, msg = verify_from_img(filename, doctype)
    return is_valid, msg



def validate_doc(doctype: str, filename: str) -> bool:
    doc_types = ['driver_license', 'passport', 'id', 'sat']
    if doctype not in doc_types:
        print("invalid doctype")
        return False
    # elif (filename[-4:] != ".jpg") or (filename[-4:] != ".png") or (filename[-5:] != ".jpeg") or (filename[-4:] != ".pdf"):
    #     print("invalid extension", filename[-4:])
    #     return False
    
    return True



def extract_img_from_pdf(filename):
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



def verify_from_img(filename: str, doctype: str='driver_license') -> tuple[bool, str]:
    if not validate_doc(doctype, filename):
        print("doc type is not valid", doctype)
        return False, "wrong_format"
        
    if filename[-4:] == '.pdf':
        image = extract_img_from_pdf(filename)
    else:
        image = cv2.imread(filename)

    if image is None:
        print("could not find image")
        return False, "wrong_format"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    # cv2.imwrite('threshold_image.jpg', thresh1)
    # os.remove('threshold_image.jpg')

    try:
        pytesseract.pytesseract.tesseract_cmd = rf'{USERPROFILE}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    except Exception:
        print("Please install tesseract-ocr for image recognition to work")
        return False, "text_not_recognizeable"

    extracted_text = pytesseract.image_to_string(thresh1, lang='rus')

    get_credentials = {
        'id': credentials.id_card,
        'driver_license': credentials.driver_license,
        'passport': credentials.passport,
        'sat': credentials.sat,
    }
    creds, msg, ok = get_credentials[doctype](extracted_text)

    if not ok:
        return False, msg
    else:
        return check[doctype](creds)




def verify_from_pdf(filename: str, doctype: str = 'driver_license') -> tuple[bool, str]:
    if not validate_doc(doctype, filename):
        return False, "wrong_format"
    elif filename[-4:] == '.pdf':
        return False, "wrong_format"
    
    reader = PdfReader(filename) 
    print(len(reader.pages)) 
    page = reader.pages[0] 

    extracted_text = page.extract_text() 
    print(extracted_text)

    get_credentials = {
        'id': credentials.id_card,
        'driver_license': credentials.driver_license,
        'passport': credentials.passport,
        'sat': credentials.sat,
    }
    creds, msg, ok = get_credentials[doctype](extracted_text)

    if not ok:
        return False, msg
    else:
        return check[doctype](creds)





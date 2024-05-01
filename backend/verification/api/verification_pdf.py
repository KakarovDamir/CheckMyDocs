from pypdf import PdfReader 
import re

import credentials
 
def verify_pdf(filename: str, doctype: str = 'driver_license') -> tuple[bool, dict]:
    reader = PdfReader(filename) 
    print(len(reader.pages)) 
    page = reader.pages[0] 

    extracted_text = page.extract_text() 
    print(extracted_text)

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
from pypdf import PdfReader 
import re

from re_patterns import *

def verify_pdf(filename: str, doctype: str = 'driver_license', filetype: str = 'pdf'):
    reader = PdfReader(filename) 
        
    # printing number of pages in pdf file 
    print(len(reader.pages)) 

    page = reader.pages[0] 

    extracted = page.extract_text() 
    print(extracted)

    issue_date = re.findall(issue_date_pattern, extracted)
    doc_number = re.findall(doc_number_pattern, extracted)
    ssn = re.findall(ssn_pattern, extracted)

    print()
    print()
    print()
    print()

    print("issue date: ", issue_date[0].strip())
    print("doc number: ", doc_number[0].strip())
    print("ssn: ", ssn[0].strip())
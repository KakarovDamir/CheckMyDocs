import re

from api.re_patterns import *

def check_nulls(*credentials) -> bool:
    for credential in credentials:
        if (not credential) or (credential.strip() == "") or (credential is None):
            return False
    return True


def id_card(extracted_text: str) -> tuple[dict, str, bool]:
    try:
        doc_number = re.findall(doc_number_pattern, extracted_text)[0].strip()
        ssn = re.findall(id_ssn_pattern, extracted_text)[0].strip()
        issue_date = re.findall(issue_date_pattern, extracted_text)[0].strip()
    except IndexError:
        return None, "text_not_recognizeable", False
    

    if not check_nulls(issue_date, doc_number, ssn):
        return None, "text_not_recognizeable", False
    
    cred_obj = {
        "issue_date": issue_date,
        "doc_number": doc_number,
        "ssn": ssn
    }

    return cred_obj, "", True



def driver_license(extracted_text: str) -> tuple[dict, str, bool]:
    try:
        license_number = re.findall(license_number_pattern, extracted_text)[0].strip()
        valid_date = re.findall(valid_date_pattern, extracted_text)[0][3:].strip()
    except IndexError:
        return None, "text_not_recognizeable", False
    
    if not check_nulls(license_number, valid_date):
        return None, "text_not_recognizeable", False


    cred_obj = {
        "license_number": license_number,
        "valid_date": valid_date
    }

    return cred_obj, "", True


# TODO: implement passport verification
def passport(extracted_text: str) -> tuple[dict, str, bool]:
    return None, "text_not_recognizeable", False


def sat(extracted_text: str) -> tuple[dict, str, bool]:
    try:
        unique_number = re.findall(unique_number_pattern, extracted_text)[0].strip()
        sat_ssn = re.findall(sat_ssn_pattern, extracted_text)[0][1:].strip()
        sat_ict = re.findall(sat_ict_pattern, extracted_text)[0][1:].strip()
    except IndexError:
        return None, "text_not_recognizeable", False
    
    if not check_nulls(unique_number, sat_ssn, sat_ict):
        return None, "text_not_recognizeable", False

    cred_obj = {
        "unique_number": unique_number,
        "sat_ssn": sat_ssn,
        "sat_ict": sat_ict
    }

    return cred_obj, "", True

    # return None, "text_not_recognizeable", False
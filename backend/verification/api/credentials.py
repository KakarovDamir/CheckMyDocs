import re

from re_patterns import *

def check_nulls(*credentials) -> bool:
    for credential in credentials:
        if (not credential) or (credential.strip() == "") or (credential is None):
            return False
    return True


def id_card(extracted_text: str) -> tuple[dict, str, bool]:
    issue_date = re.findall(issue_date_pattern, extracted_text)[0].strip()
    doc_number = re.findall(doc_number_pattern, extracted_text)[0].strip()
    ssn = re.findall(ssn_pattern, extracted_text)[0].strip()

    if not check_nulls(issue_date, doc_number, ssn):
        return None, "text_not_recognizeable", False
    
    cred_obj = {
        "issue date: ", issue_date,
        "doc number: ", doc_number,
        "ssn: ", ssn
    }

    return cred_obj, "", True



def driver_license(extracted_text: str) -> tuple[dict, str, bool]:
    license_number = re.findall(license_number_pattern, extracted_text)[0].strip()
    valid_date = re.findall(valid_date_pattern, extracted_text)[0][3:].strip()

    if not check_nulls(license_number, valid_date):
        return None, "text_not_recognizeable", False

    cred_obj = {
        "license number: ", license_number,
        "valid date: ", valid_date
    }

    return cred_obj, "", True



def passport(extracted_text: str) -> tuple[dict, str, bool]:
    pass


def sat(extracted_text: str) -> tuple[dict, str, bool]:
    pass
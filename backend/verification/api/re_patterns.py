# id card patterns
issue_date_pattern = r"\d\d\.\d\d\.\d\d\d\d - \d\d\.\d\d\.\d\d\d\d" 
doc_number_pattern = r"[^a-zA-Z0-9]\d\d\d\d\d\d\d\d\d[^a-zA-Z0-9]"
id_ssn_pattern = r"\d\d\d\d\d\d\d\d\d\d\d\d"


# driver license patterns
surname_pattern = r'1\. [А-Я][а-я]+ \/'
name_pat_pattern = r'2\. [А-Я][а-я]+ [А-Я][а-я]+ \/'

license_number_pattern = r'\d{10}'
valid_date_pattern = r'4а\) \d\d\.\d\d\.\d\d\d\d'


# sat patterns
unique_number_pattern = r'\d{1,2}-\d\d\d\d-\d\d{1,2}-\d{9,10}-\d{1,2}-\d{1,2}'
sat_ssn_pattern = r":\d{12}"
sat_ict_pattern = r"-\d{9}"


# TODO passport patterns 

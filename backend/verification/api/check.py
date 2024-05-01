


def check_id_card(credentials: dict) -> tuple[bool, str]:
    return True, "valid"
    


def check_driver_license(credentials: dict) -> tuple[bool, str]:
    return True, "valid"


def check_passport(credentials: dict) -> tuple[bool, str]:
    pass


def check_sat(credentials: dict) -> tuple[bool, str]:
    pass


check = {
    'driver_license': check_driver_license,
    'passport': check_passport,
    'id': check_id_card,
    'sat': check_sat,
    }
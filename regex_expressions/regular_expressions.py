import re 


def validate_username(userName):
    regular_expresion = r"^[a-zA-Z]+$"
    return bool(re.match(regular_expresion, userName))

import re 

def validate_username(userName):
    regular_expresion = r"^[a-zA-Z]+ [a-zA-Z]+$"
    regular_expresion2 = r"^[a-zA-Z]+$"
    
    if (re.match(regular_expresion, userName) or re.match(regular_expresion2, userName)):
        return True
    else :
        return False

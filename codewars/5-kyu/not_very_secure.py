import re

def alphanumeric(password):
    if re.match("^[a-zA-Z0-9]+$", password):
        return True
    else:
        return False

print(alphanumeric('PassW0rd'))
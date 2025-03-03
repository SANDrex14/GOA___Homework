
import re

def validate_username(username):
    pattern = r'^[a-z0-9_]{4,16}$'
    if re.match(pattern, username):
        return True
    else:
        return False

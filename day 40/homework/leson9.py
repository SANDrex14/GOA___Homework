def get_issuer(number):
    number_str = str(number) 
    length = len(number_str)
    
    if (number_str.startswith('34') or number_str.startswith('37')) and length == 15:
        return "AMEX"
    
    elif number_str.startswith('6011') and length == 16:
        return "Discover"
    
    elif number_str[:2] in ['51', '52', '53', '54', '55'] and length == 16:
        return "Mastercard"
    
    elif number_str.startswith('4') and (length == 13 or length == 16):
        return "VISA"
    
    return "Unknown"

def even_or_odd(s):
    even_sum = 0
    odd_sum = 0
    
    for char in s:
        digit = int(char) 
        if digit % 2 == 0:
            even_sum += digit  
        else:
            odd_sum += digit 
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
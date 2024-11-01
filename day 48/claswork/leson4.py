def solve(s):
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    special_count = 0
    
    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1
        else:
            special_count += 1
    
    return [uppercase_count, lowercase_count, number_count, special_count]


result = solve("*'&ABCDabcde12345")
print(result)  

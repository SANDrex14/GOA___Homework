def add(num1, num2):
  
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    max_len = max(len(str_num1), len(str_num2))
    str_num1 = str_num1.zfill(max_len)
    str_num2 = str_num2.zfill(max_len)
    
    result = ""
    
    for i in range(max_len):
        digit_sum = int(str_num1[i]) + int(str_num2[i])
        result += str(digit_sum % 10) 
    
    return int(result)  

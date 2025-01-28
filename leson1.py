# 1
def sum_mix(arr):
    return sum(int(x) for x in arr)

# 2
def double_char(s):
    return ''.join(c * 2 for c in s)

# 3
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

# 4
def reverse_words(s):
    words = s.split()
    
    words_reversed = words[::-1]
    
    return ' '.join(words_reversed)

# 5
def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    
    num_a = int(a)
    num_b = int(b)
    
    result = num_a + num_b
    
    return str(result)

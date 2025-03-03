# 1

def shortcut(s):
    return ''.join([i for i in s if i not in 'aeiou'])

# 2

def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]


# 4) 
def odd_nums(arr):
    return [i*2 if i % 2 != 0 else i for i in arr]

# 5
def square_digits(num):
    digits = str(num)
    
    squared_digits = ''.join(str(int(digit)**2) 
    for digit in digits)
    
    return int(squared_digits)

# 6
def distinct(seq):
    return sorted(set(seq), key = seq.index)

# 7
def largest_num(arr):
    return int(''.join(str(i) for i in sorted(arr, reverse=True)))

# 8
def even_numbers(arr, n):
    evens = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
    return evens[-n:]
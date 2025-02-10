#Codewars solutions!

#https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python

def even_numbers(arr,n):
    even_numbers = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_numbers.append(arr[i])
    return even_numbers[-n:]

#https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/python

def sum_of_n(n):
    list = []
    num = 0
    num2 = 0
    list.append(0)
    if n > 0:
        for i in range(n):
            num2 = num2 + 1
            num = num + num2
            list.append(num)
    elif n < 0:
        for i in range(n * (-1)):
            num2 = num2 - 1
            num = num + num2
            list.append(num)
    return list
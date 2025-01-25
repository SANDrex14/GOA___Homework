def sum_even_numbers(seq):
    even_numbers = [num for num in seq if isinstance(num, int) and num % 2 == 0]
    
    return sum(even_numbers)

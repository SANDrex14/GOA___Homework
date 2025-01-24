
def is_even(n):
    if isinstance(n, float) and n != int(n):
        return False  
    return n % 2 == 0

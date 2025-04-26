# 1-------------------------------------
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n


# 2-----------------------------------------
def is_int_array(arr):
    if not isinstance(arr, list):
        return False
    for x in arr:
        if not (isinstance(x, int) or (isinstance(x, float) and x.is_integer())):
            return False
    return True



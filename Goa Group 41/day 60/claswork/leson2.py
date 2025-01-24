def fake_bin(x):
    result = ''
    for digit in x:
        if digit < '5':
            result += '0'
        else:
            result += '1'
    return result
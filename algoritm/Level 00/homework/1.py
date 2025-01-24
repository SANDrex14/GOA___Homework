def count_multiples(a, b, c):
    if c == 0:
        return "No No No"
    
    start, end = min(a, b), max(a, b)

    if start % c == 0:
        start_div = start // c
    else:
        start_div = start // c + 1

    if end % c == 0:
        end_div = end // c
    else:
        end_div = end // c

    return max(0, end_div - start_div + 1)

# ტესტირება
a, b, c = 1, 10, 3
print(count_multiples(a, b, c))

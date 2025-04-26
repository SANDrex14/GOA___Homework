# 1-------------------------------------
def min_length_num(num_dig, ord_max):
    def S(n):
        return sum(i * (n - i + 1) for i in range(1, n + 1))
    
    for i in range(1, ord_max + 1):
        if len(str(S(i))) == num_dig:
            return [True, i]
    return [False, -1]

# 2-----------------------------------------

# 3---------------------------------------

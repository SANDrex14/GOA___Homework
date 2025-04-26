# 1------------------------------------
def branch(n):
    x, s = 1, 2
    while True:
        for i in range(4):
            x += s
            if x >= n:
                return i
        s += 2

# 2------------------------------------
def to_binary(n):
    return int(bin(n)[2:])


# 3--------------------------------------------


def josephus_survivor(n, k):
    survivor = 0
    for i in range(2, n + 1):
        survivor = (survivor + k) % i
    return survivor + 1

# 4-------------------------------------

def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) 
print(move_zeros([0, 0, 1, 2, 3]))        
print(move_zeros([1, 2, 3]))              
print(move_zeros([0, 0, 0]))             


# 5------------------------


def sum_strings(x, y):
    if not x: x = '0'
    if not y: y = '0'

    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        total = int(x[i]) + int(y[i]) + carry
        result.append(str(total % 10))
        carry = total // 10

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1]).lstrip('0') or '0'

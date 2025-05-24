# 1--------------------------------
def unique_sum(lst):
    if lst:
       return sum(set(lst)) 

# 2--------------------------------
def add(l):
    return [sum(l[:i+1]) for i in range(len(l))]


# 3--------------------------------
from gmpy2 import is_prime
def total(arr):
    return sum([[0,n][is_prime(i)] for i,n in enumerate(arr)])
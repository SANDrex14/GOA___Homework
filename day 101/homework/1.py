# 1) Find the difference between two sets: Create a new set containing elements that are present in the first set but not in the second.
def difference(set1, set2):
    return set1 - set2

# 2) Create a random number generator without duplicates: Use a set to prevent duplicate random numbers.
def random_no_duplicates(n):
    import random
    return set(random.sample(range(1, 101), n))


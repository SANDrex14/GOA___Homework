# 1
def shorten_to_date(long_date):
    return long_date.split(',')[0]

# 2
def find_average(nums):
    if not nums: 
        return 0
    return sum(nums) / len(nums)
# 3

def replace_dots(str):
    return str.replace('.', '-')

# 4
def find_needle(haystack):
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            return f"found the needle at position {i}"


haystack = ["hy", "jun", "hayn", "huy", "moron", "needle", "unk"]
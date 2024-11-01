def make_negative(number):
    # Return the number as negative if it's positive, otherwise return it unchanged
    return -abs(number) if number > 0 else number

def reverse_words(s):
    words = s.split()
    
    words_reversed = words[::-1]
    
    return ' '.join(words_reversed)

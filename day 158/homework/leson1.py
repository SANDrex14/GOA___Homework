# 1-------------------------------------
def proofread(st):
    st = st.replace('ei', 'ie')
    sentences = st.lower().split('.')
    corrected = []
    for s in sentences:
        s = s.strip()
        if s:
            corrected.append(s[0].upper() + s[1:])
    return '. '.join(corrected) + ('.' if st.strip().endswith('.') else '')


# 2-----------------------------------------
def sum_triangular_numbers(n):
    if n < 0:
        return 0
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += i * (i + 1) // 2
    return sum_


# 3---------------------------------------
def sum_triangular_numbers(n):
    if n < 0:
        return 0
    sum_ = 0
    for i in range(1, n + 1):
        sum_ += i * (i + 1) // 2
    return sum_

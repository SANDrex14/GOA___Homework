def categorize_age(age):
    if age < 13:
        return "ბავშვი"
    elif 13 <= age <= 19:
        return "თინეიჯერი"
    elif 20 <= age <= 64:
        return "ზრდასრული"
    else:
        return "ხანდაზმული"

age = int(input("შეიყვანეთ ასაკი: "))
print(categorize_age(age))

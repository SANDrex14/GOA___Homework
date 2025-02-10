ages = []
num_members = int(input("შეიყვანეთ ოჯახის წევრების რაოდენობა: "))

for i in range(num_members):
    age = int(input(f"შეიყვანეთ {i+1}-ე ოჯახის წევრის ასაკი: "))
    ages.append(age)


future_ages = [age + 20 for age in ages]


for i, future_age in enumerate(future_ages):
    print(f"{i+1}-ე ოჯახის წევრი 20 წლის შემდეგ იქნება {future_age} წლის.")

my_age = 25 

user_age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if user_age == my_age:
    print(True)
else:
    user_age = int(input("შეიყვანეთ თქვენი ასაკი კიდევ ერთხელ: "))
    if user_age == my_age:
        print(True)
    else:
        print(False)


my_age = 25  

for attempt in range(2):
    user_age = int(input("შეიყვანეთ თქვენი ასაკი: "))

    if user_age == my_age:
        print(True)
        break
    else:
        print(False)

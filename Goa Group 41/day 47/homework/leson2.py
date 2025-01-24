def check_number(num):
    if num > 0:
        return "რიცხვი დადებითია"
    elif num < 0:
        return "რიცხვი უარყოფითია"
    else:
        return "რიცხვი ნულია"

num = float(input("შეიყვანეთ რიცხვი: "))
print(check_number(num))

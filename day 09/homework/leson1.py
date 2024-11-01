def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "დარწმუნდით, რომ არ გაწვდეთ 0-ით!"
    return x / y

try:
    num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიტანეთ მეორე რიცხვი: "))

    # მათემატიკური ოპერაციები
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")

except ValueError:
    print("გთხოვთ, შეიტანოთ ვალიდური რიცხვი.")

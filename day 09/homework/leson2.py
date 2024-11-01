def calculator():
    print("კალკულატორი")
    print("თქვენ შეგიძლიათ ჩაწეროთ '+' (დამატება), '-' (შესაკრავება), '*' (გამრავლება) ან '/' (გამყოფი).")

    # მომხმარებლისგან ორი რიცხვის შეყვანა
    try:
        num1 = float(input("შეიტანეთ პირველი რიცხვი: "))
        num2 = float(input("შეიტანეთ მეორე რიცხვი: "))
        operation = input("შეიტანეთ ოპერაცია (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("დარწმუნდით, რომ არ გაწვდეთ 0-ით!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("არასწორი ოპერაცია. გთხოვთ, შეიტანეთ +, -, *, ან /.")
    
    except ValueError:
        print("გთხოვთ, შეიტანოთ ვალიდური რიცხვი.")

# კალკულატორის გაწვდვა
calculator()

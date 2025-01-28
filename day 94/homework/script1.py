# 1)Logical Operators

def check_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    return False

# 2)Prompt: Email verification

def email_verification():
    email = input("Enter your email: ")
    print("access granted")

# 3)Comparison Operators

def compare_numbers(a, b):
    if a == b:
        print("Numbers are equal")
    elif a > b:
        print("First number is greater")
    else:
        print("Second number is greater")

# 4)Conditional Statements

def financial_planning(age, gender, income):
    if age >= 18:
        if gender == "female":
            if income > 5000:
                print("Your financial status is secured")
            elif income > 3000:
                print("Financial position is stable. A better plan is needed.")
            else:
                print("You need to improve your financial plan.")
        elif gender == "male":
            if income > 6000:
                print("You are ready for investments!")
            elif income > 4000:
                print("Income is stable.")
            else:
                print("You need to improve your financial plan.")
    else:
        print("Get an education and then start investing")

# 5)Switch (Emulated)

def switch_case(option):
    switch = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected",
    }
    return switch.get(option, "Invalid option")

# 6)Ternary Operator

def success_message(age, grade):
    if age >= 18 and grade > 50:
        print("You are successful")
    elif age >= 18:
        print("You need more study")
    else:
        print("You're a child, but you can succeed")

# 7)For Loop

def prime_numbers_sum():
    prime_sum = 0
    for num in range(2, 101):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num
    print("Sum of prime numbers:", prime_sum)

# 8)While Loop

def prime_numbers_sum_while():
    prime_sum = 0
    num = 2
    while num <= 100:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num
        num += 1
    print("Sum of prime numbers:", prime_sum)

# 9)Break and Continue Operators

def break_continue_example():
    for num in range(1, 51):
        if num == 25:
            continue
        if num % 2 == 0:
            print(num)

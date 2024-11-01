def reverse_numbers(numbers):
    return numbers[::-1]

user_input = input("შეიყვანეთ რიცხვები, გამოყავით ისინი მძიმით (,): ")
number_list = [int(num) for num in user_input.split(",")]
reversed_list = reverse_numbers(number_list)

print("შებრუნებული რიცხვების სია:", reversed_list)

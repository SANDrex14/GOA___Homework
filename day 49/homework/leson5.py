def calculate_average(numbers):
    return sum(numbers) / len(numbers)

user_input = input("შეიყვანეთ რიცხვები, გამოყავით ისინი მძიმით (,): ")
number_list = [float(num) for num in user_input.split(",")]
average_value = calculate_average(number_list)

print(f"საშუალო მნიშვნელობა: {average_value:.2f}")

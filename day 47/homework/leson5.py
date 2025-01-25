def find_average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("შეიყვანეთ რიცხვები მძიმით გამოყოფილი: ").split(',')))
print(f"საშუალო რიცხვი: {find_average(numbers)}")

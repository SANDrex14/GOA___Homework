numbers = []
for i in range(4):
    num = float(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))
    numbers.append(num)


addition = sum(numbers)
subtraction = numbers[0] - sum(numbers[1:])
multiplication = 1
for num in numbers:
    multiplication *= num
division = numbers[0]
for num in numbers[1:]:
    if num != 0:
        division /= num
    else:
        division = "არ შეიძლება გაწვდო 0-თან"


print(f"რიცხვების ჯამი: {addition}")
print(f"რიცხვების სხვაობა: {subtraction}")
print(f"რიცხვების გამრავლება: {multiplication}")
print(f"რიცხვების გაწვდვა: {division}")

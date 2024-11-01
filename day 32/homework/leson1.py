def simple_calculator(num1, num2, operation):
    if operation == "დამატება":
        return num1 + num2
    elif operation == "გამოკლება":
        return num1 - num2
    elif operation == "გამრავლება":
        return num1 * num2
    elif operation == "გაყოფა":
        if num2 == 0:
            return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
        else:
            return num1 / num2
    else:
        return "შეცდომა: გაუგებარი ოპერაცია"

result1 = simple_calculator(10, 5, "დამატება")
print("10 + 5 =", result1)

result2 = simple_calculator(10, 5, "გამოკლება")
print("10 - 5 =", result2)

result3 = simple_calculator(10, 5, "გამრავლება")
print("10 * 5 =", result3)

result4 = simple_calculator(10, 0, "გაყოფა")
print("10 / 0 =", result4)

result5 = simple_calculator(10, 5, "გაყოფა")
print("10 / 5 =", result5)

result6 = simple_calculator(10, 5, "ბოლო ოპერაცია")
print("10, 5, 'ბოლო ოპერაცია' =", result6)

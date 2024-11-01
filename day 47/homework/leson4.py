def find_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

numbers = list(map(int, input("შეიყვანეთ რიცხვები მძიმით გამოყოფილი: ").split(',')))
even, odd = find_even_odd(numbers)
print(f"ლუწი რიცხვები: {even}")
print(f"კენტი რიცხვები: {odd}")


# map() ფუნქცია გამოყენებულია იმისთვის, რომ სიის თითოეული ელემენტი გადააკეთოს int ტიპის რიცხვად.
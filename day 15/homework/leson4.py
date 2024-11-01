# file: while_guess_number.py
correct_number = int(input("შეიყვანეთ რიცხვი, რომელიც მე უნდა გამოვიცნო: "))

while True:
    guess = int(input("შეიყვანეთ თქვენი გამოცნობა: "))
    if guess == correct_number:
        print("გილოცავთ, სწორად გამოიცანით!")
        break
    else:
        print("არასწორია, სცადეთ ხელახლა.")

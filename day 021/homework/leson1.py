correct_number = 42  

user_guess = int(input("შეიყვანეთ რიცხვი 1-დან 100-მდე: "))

while user_guess != correct_number:
    if user_guess < 1 or user_guess > 100:
        print("რიცხვი უნდა იყოს 1-დან 100-მდე!")
    elif user_guess < correct_number:
        print("თქვენი რიცხვი ნაკლებია, სცადეთ უფრო დიდი რიცხვი.")
    elif user_guess > correct_number:
        print("თქვენი რიცხვი დიდია, სცადეთ უფრო მცირე რიცხვი.")
    
    user_guess = int(input("სცადეთ კიდევ ერთხელ, შეიყვანეთ რიცხვი 1-დან 100-მდე: "))

print("გილოცავთ! თქვენ გამოიცანით სწორი რიცხვი:", correct_number)

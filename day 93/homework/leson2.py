def get_transport_recommendation():
    name = input("შეიყვანეთ თქვენი სახელი: ")
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))
    distance = float(input("სამუშაო ადგილამდე მანძილი (კმ-ში): "))
    work_days = int(input("სამუშაო დღეების რაოდენობა კვირაში (0-დან 7-მდე): "))

    if age < 16:
        print("გთხოვთ, მოითხოვოთ გამგზავრების ნებართვა უფროსისგან.")
        return

    if age >= 16 and age < 65:
        if distance <= 5:
            transport = "ველოსიპედი"
        elif distance <= 20:
            transport = "მანქანა"
        else:
            transport = "მატარებელი"

        print(f"{name}, რეკომენდირებული ტრანსპორტია: {transport}")

        if work_days >= 5:
            print("სთხოვეთ შეღავათები ტრანსპორტზე.")
    else:
        print(f"{name}, გთხოვთ, გაიაროთ ექიმის კონსულტაცია.")

def get_running_recommendation():
    name = input("შეიყვანეთ თქვენი სახელი: ")
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))
    daily_run = float(input("ყოველდღიური სირბილის რაოდენობა (კმ-ში): "))
    exercise_days = int(input("სავარჯიშო დღეების რაოდენობა კვირაში (0-დან 7-მდე): "))

    if age < 16 or age > 60:
        print("გთხოვთ, გაიაროთ ექიმის კონსულტაცია.")
        return

    weekly_run = daily_run * exercise_days

    if weekly_run < 20:
        print(f"{name}, შესაძლებელია მეტი ვარჯიში.")
    else:
        print(f"{name}, შესანიშნავი პროგრესი გაქვთ!")

# ძირითადი პროგრამის გაშვება
if __name__ == "__main__":
    print("აირჩიეთ პროგრამა:")
    print("1. ტრანსპორტის რეკომენდაცია")
    print("2. სირბილის რეკომენდაცია")

    choice = int(input("შეიყვანეთ არჩევანი (1 ან 2): "))
    if choice == 1:
        get_transport_recommendation()
    elif choice == 2:
        get_running_recommendation()
    else:
        print("არასწორი არჩევანი.")

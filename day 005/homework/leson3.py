name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
country = input("შეიყვანეთ თქვენი ქვეყანა: ")
city = input("შეიყვანეთ თქვენი ქალაქი: ")
favorite_color = input("შეიყვანეთ თქვენი საყვარელი ფერი: ")
favorite_car = input("შეიყვანეთ თქვენი საყვარელი მანქანა: ")
favorite_food = input("შეიყვანეთ თქვენი საყვარელი საჭმელი: ")
favorite_sport = input("შეიყვანეთ თქვენი საყვარელი სპორტი: ")

introduction = f"მე ვარ {name} {surname}, {age} წლის, მცხოვრები {city}, {country}-ში. ჩემი საყვარელი ფერი არის {favorite_color}, " \
               f"მინდა {favorite_car} მანქანა, მიყვარს {favorite_food} საჭმელი და ჩემი საყვარელი სპორტი არის {favorite_sport}."

print(introduction)

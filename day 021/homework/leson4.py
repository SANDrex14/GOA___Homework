
def check_positive_integer(value):
    return value > 0

while True:
    try:
        age = int(input("შეიყვანეთ თქვენი ასაკი (დადებითი მთელი რიცხვი): "))
        if not check_positive_integer(age):
            raise ValueError("ასაკი უნდა იყოს დადებითი მთელი რიცხვი.")
        
        driving_experience = int(input("რამდენი წელი გაქვთ მანქანის მართვის გამოცდილება? (დადებითი მთელი რიცხვი): "))
        if not check_positive_integer(driving_experience):
            raise ValueError("გამოცდილების წლები უნდა იყოს დადებითი მთელი რიცხვი.")
        
        break
    except ValueError as e:
        print(e)

if age < 18:
    print("თქვენ არ შეგიძლიათ მართვის მოწმობის აღება, რადგან ჯერ არ ხართ 18 წლის.")
elif age >= 18 and driving_experience >= 1:
    print("გილოცავთ! თქვენ გაქვთ მართვის მოწმობის აღების უფლება.")
elif age >= 18 and driving_experience < 1:
    print("თქვენ ხართ საკმარისად ზრდასრული მართვის მოწმობისთვის, მაგრამ არ გაქვთ საკმარისი გამოცდილება.")

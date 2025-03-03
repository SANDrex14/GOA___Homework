# // მომხარებელს შემოვატანინოთ რამდენი ხნით სურს დროში მოგზაურობა, ამისთვის გამოიყენეთ input.

time = int(input("How many hours do you want to travel? "))
if time <= 2:
    print("You can travel by bus.")
elif time <= 4:
    print("You can travel by train.")
elif time <= 6:
    print("You can travel by plane.")
else:
    print("You can travel by helicopter.")


    

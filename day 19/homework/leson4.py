my_name = "შენი სახელი"  

user_name = input("გთხოვთ, შეიყვანეთ თქვენი სახელი: ")

while user_name != my_name:
    print("თქვენი სახელი არ ემთხვევა.")
    user_name = input("გთხოვთ, ისევ შეიყვანეთ თქვენი სახელი: ")

print("კარგი! თქვენი სახელი არის:", user_name)

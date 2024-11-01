# 1. პროექტის აღწერა:
# პრობლემა: დაწერეთ პროგრამა, რომელიც ითვლის სტუდენტების ნიშნებს და განსაზღვრავს საუკეთესო სტუდენტს.
#  მომხმარებელი შეიყვანს სტუდენტების სახელებსა და მათ ნიშანს,
#  პროგრამა კი გამოთვლის საშუალო ნიშანს თითოეული სტუდენტისთვის და გამოაცხადებს საუკეთესოს.


def student():

    num_students = int(input("შეიყვანეთ სტუდენტების რაოდენობა!: "))
    
    students = {}
    
    for i in range(num_students):
        name = input("შეიყვანეთ სახელი: ")
        Points = input("შეიყვანეთ ნიშნები (ნიშნები გამოყავით მძიმეებით): ")
        Points_list = list(map(int, Points.split(",")))  
        average_grade = sum(Points_list) / len(Points_list)  
        students[name] = average_grade  

    Good_student = max(students, key=students.get)
    
    print(f"საუკეთესო სტუდენტი არის: {Good_student} საშუალო ნიშანი მიღო: {students[Good_student]}")


student()


# split() ფუნქცია იყოფს ტექსტს ნაწილებად გამყოფი სიმბოლოთი (სივრცე ანუ) და ქმნის სიას სიტყვებისგან.

# students.get ფუნქცია უზრუნველყოფს ამ მნიშვნელობების მიღებას, რათა max შეძლოს სწორი გასაღების პოვნა.

# map(int, grades.split(",")) ნიშნავს, რომ grades.split(",") შედეგს,
# ანუ grades სტრინგის დაყოფის შემდეგ წარმოქმნილ ელემენტების სიას, თითოეულ ელემენტს გადააქცევს int-ად.?
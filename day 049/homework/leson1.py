
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

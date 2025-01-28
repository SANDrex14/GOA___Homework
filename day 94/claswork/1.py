def grade_student():
    subject1 = int(input("Enter the grade for Subject 1: "))
    subject2 = int(input("Enter the grade for Subject 2: "))
    subject3 = int(input("Enter the grade for Subject 3: "))
    average = (subject1 + subject2 + subject3) / 3
    if 90 < average <= 100:
        print("A")
    elif 70 < average <= 80:
        print("B")
    elif 50 < average <= 65:
        print("C")
    elif 25 < average <= 50:
        print("D")
    else:
        print("წადი ისწავლე და მერე მოდი")

grade_student()

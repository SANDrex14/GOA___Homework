
def check_valid_score(score):
    return 0 <= score <= 100

while True:
    try:
        midterm_score = float(input("შეიყვანეთ შუალედური გამოცდის ქულა (0-დან 100-მდე): "))
        if not check_valid_score(midterm_score):
            raise ValueError("ქულა უნდა იყოს 0-დან 100-მდე.")
        
        final_exam_score = float(input("შეიყვანეთ დასკვნითი გამოცდის ქულა (0-დან 100-მდე): "))
        if not check_valid_score(final_exam_score):
            raise ValueError("ქულა უნდა იყოს 0-დან 100-მდე.")
        
        project_score = float(input("შეიყვანეთ პროექტის ქულა (0-დან 100-მდე): "))
        if not check_valid_score(project_score):
            raise ValueError("ქულა უნდა იყოს 0-დან 100-მდე.")
        
        break
    except ValueError as e:
        print(e)

average_score = (midterm_score * 0.2) + (final_exam_score * 0.4) + (project_score * 0.4)

if average_score >= 70:
    print(f"გილოცავთ! თქვენ ჩააბარეთ კურსი. თქვენი საშუალო ქულა არის: {average_score:.2f}")
else:
    print(f"სამწუხაროდ, თქვენ ვერ ჩააბარეთ კურსი. თქვენი საშუალო ქულა არის: {average_score:.2f}")

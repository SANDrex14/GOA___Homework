def calculate_future_age():
  
    try:
        age = int(input("შეიტანეთ თქვენი ასაკი: "))
        
       
        future_age = age + 10
        
 
        print(f"10 წლის შემდეგ თქვენ იქნებით {future_age} წლის.")
    
    except ValueError:
        print("გთხოვთ, შეიტანოთ ვალიდური ასაკი (რიცხვი).")


calculate_future_age()

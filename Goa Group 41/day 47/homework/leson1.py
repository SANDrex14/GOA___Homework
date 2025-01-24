def word_count(text):
    words = text.split()  
    return len(words)

text = input("შეიყვანეთ ტექსტი: ")
print(f"სიტყვების რაოდენობა ტექსტში: {word_count(text)}")

# split() ფუნქცია იყოფს ტექსტს ნაწილებად გამყოფი სიმბოლოთი (სივრცე ანუ) და ქმნის სიას სიტყვებისგან.
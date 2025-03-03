#    2) მომხამრებელს შემოატანინეთ რიცხვი შემდეგ კი დაბეჭდეთ მომხმარებლის შემოტანილ რიცხვამდე ყველა რიცხვის ჯამი

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(sum)
    
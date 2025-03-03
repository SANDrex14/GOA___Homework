
# // შექმენით ობიექტის კონსტრუქტორი რომელსაც გადაეცემა მომხმარებლის შესახებ ინფორმაცია(სახელი, გვარი, ასაკი)  ამ კონსტრუქტორში შექმენით მეთოდი რომელიც მომხმარებელს ამოგზაურებს დროში იდმენი ხნით რამდენიც მას სურს, და მის ასაკს გაზრდის იმდენით რამდენითაც მას სურს


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def birthday(self, years):
        self.age += years
        return self.age

    def birthday(self, years):
        self.age += years
        return self.age

    def birthday(self, years):
        self.age += years
        

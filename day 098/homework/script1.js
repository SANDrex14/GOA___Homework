function Person(name, age, profession) {
    this.name = name;
    this.age = age;
    this.profession = profession;

    this.introduce = function() {
        console.log(`Hi, I'm ${this.name}, a ${this.age}-year-old ${this.profession}.`);
    };
}

const person1 = new Person("Alice", 30, "Software Engineer");
person1.introduce();

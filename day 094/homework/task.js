// Rest Operator Function
function addItems(...items) {
    return items.reduce((sum, item) => sum + item, 0);
}

// Spread Operator - Array Cloning and Merging
function mergeArrays() {
    const array1 = [1, 2, 3, 4, 5];
    const array2 = [...array1, 6, 7, 8];
    console.log(array2);
}

// Spread Operator - Convert Array to Object
function arrayToObject(...items) {
    return { ...items };
}

// Spread Operator - Clone Object
function clonePerson() {
    const person = { name: "John", age: 30 };
    const student = { ...person, course: "Computer Science" };
    console.log(student);
}

// Class Person
class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    getFullName() {
        return `${this.firstName} ${this.lastName}`;
    }
}

// Student Class Extending Person
class Student extends Person {
    constructor(firstName, lastName, course, duration) {
        super(firstName, lastName);
        this.course = course;
        this.duration = duration;
    }
    printDetails() {
        console.log(`Name: ${this.getFullName()}, Course: ${this.course}, Duration: ${this.duration} years`);
    }
    set updateCourse(newCourse) {
        this.course = newCourse;
    }
    get studentInfo() {
        return `Student: ${this.getFullName()}, Course: ${this.course}, Duration: ${this.duration} years`;
    }
}

// Testing Functions
console.log(addItems(1, 2, 3, 4, 5));
mergeArrays();
console.log(arrayToObject(1, 2, 3, 4, 5));
clonePerson();

const student = new Student("Jane", "Doe", "Mathematics", 3);
student.printDetails();
student.updateCourse = "Physics";
console.log(student.studentInfo);

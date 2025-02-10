student = {
    name: "John Doe",
    age: 21,
    faculty: "Computer Science",
    course: 3,
    gpa: 3.8
};

console.log(student);

console.log(student.name);
console.log(student["age"]);
console.log(student.faculty);
console.log(student["course"]);
console.log(student.gpa);

console.log(`${student.name} is a ${student.age}-year-old student in the ${student.faculty} faculty, currently in year ${student.course}, with an average GPA of ${student.gpa}.`);

function simple_calculator(num1, num2, operation) {
    if (operation === "დამატება") {
        return num1 + num2;
    } else if (operation === "გამოკლება") {
        return num1 - num2;
    } else if (operation === "გამრავლება") {
        return num1 * num2;
    } else if (operation === "გაყოფა") {
        if (num2 === 0) {
            return "შეცდომა: ნულზე გაყოფა შეუძლებელია";
        }
        return num1 / num2;
    } else {
        return "შეცდომა: უცნობი ოპერაცია";
    }
}

console.log(simple_calculator(10, 5, "დამატება")); 
console.log(simple_calculator(10, 5, "გამოკლება"));
console.log(simple_calculator(10, 5, "გამრავლება")); 
console.log(simple_calculator(10, 5, "გაყოფა")); 
console.log(simple_calculator(10, 0, "გაყოფა")); 
console.log(simple_calculator(10, 5, "უცნობი")); 

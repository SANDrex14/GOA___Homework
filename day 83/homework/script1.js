function checkNumber(num) {
    if (num % 2 === 0) {
        console.log("რიცხვი არის ლუწი");
    } else {
        console.log("რიცხვი არის კენტი");
    }
}

let userInput = prompt("შეიყვანეთ რიცხვი:");
checkNumber(parseInt(userInput));

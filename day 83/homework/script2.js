function checkTemperature(temp) {
    if (temp <= 0) {
        console.log("ტემპერატურა არის ცივი");
    } else if (temp > 0 && temp <= 25) {
        console.log("ტემპერატურა არის ზომიერი");
    } else {
        console.log("ტემპერატურა არის ცხელი");
    }
}

let userInput = prompt("შეიყვანეთ ტემპერატურა ცელსიუსში:");
checkTemperature(parseFloat(userInput));

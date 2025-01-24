function determineGrade(score) {
    if (score >= 90 && score <= 100) {
        console.log("შეფასება: A");
    } else if (score >= 80 && score <= 89) {
        console.log("შეფასება: B");
    } else if (score >= 70 && score <= 79) {
        console.log("შეფასება: C");
    } else if (score >= 60 && score <= 69) {
        console.log("შეფასება: D");
    } else if (score >= 0 && score < 60) {
        console.log("შეფასება: F");
    } else {
        console.log("გთხოვთ, შეიყვანეთ სწორი ქულა (0-100).");
    }
}

// გამოსაყენებლად, რომ გამოიყენოთ ეს ფუნქცია:
let userInput = prompt("შეიყვანეთ ქულა (0-100):");
determineGrade(parseInt(userInput));

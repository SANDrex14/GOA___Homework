function guessPassword() {
    const password = "Group 41 is best";
    let attempts = 3;
  
    while (attempts > 0) {
      const userInput = prompt("შეიყვანეთ პაროლი:");
      
      if (userInput === password) {
        alert("თქვენი შეყვანილი პაროლი სწორია");
        return;
      }
  
      attempts--;
  
      if (attempts > 0) {
        alert(`პაროლი არასწორია. დაგრჩათ ${attempts} ცდა.`);
      } else {
        alert("თქვენ ამოგეწურათ ცდების რაოდენობა");
      }
    }
  }
  
  guessPassword();
  
function User(name, lastName, phoneNumber, email, password, confrim_password) {
    this.name = name;
    this.lastName = lastName;
    this.phoneNumber = phoneNumber;
    this.email = email;
    this.password = password;
    this.confrim_password =  confrim_password
}

const user1 = new User("სანდრო", "ჩაფიძე", "ნომერი", "მეილი", "პაროლი", "რაღაცის პაროლი");
const user2 = new User("გიორგი", "ვარადაშვილი", "ნომერი", "მეილი", "პაროლი", "რაღაცის პაროლი");
const user3 = new User("დავით", "ჯანეზაშვილი", "ნომერი", "მეილი", "პაროლი", "რაღაცის პაროლი");

console.log(user1);
console.log(user2);
console.log(user3);


























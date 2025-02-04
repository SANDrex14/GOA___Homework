function User(username, email, password) {
    this.username = username;
    this.email = email;
    this.password = password;

    this.changePassword = function(newPassword) {
        this.password = newPassword;
    };

    this.getDetails = function() {
        return `Username: ${this.username}, Email: ${this.email}`;
    };
}

const user1 = new User("john_doe", "john@example.com", "password123");
const user2 = new User("jane_doe", "jane@example.com", "securepass");

console.log(user1.getDetails());
console.log(user2.getDetails());

user1.changePassword("newpassword456");
console.log("Password changed for user1.");

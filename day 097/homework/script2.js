const customer = {
    firstName: "John",
    lastName: "Doe",
    email: "john.doe@example.com",
    fullName() {
      return `${this.firstName} ${this.lastName}`;
    },
    updateEmail(newEmail) {
      this.email = newEmail;
    }
  };
  
  console.log(customer.fullName());
  customer.updateEmail("john.new@example.com");
  console.log(customer.email);
  
let product1 = {
    productName: "Laptop",
    price: 1000,
    quantity: 5,
    isAvailable: true
  };
  
  let product2 = {
    productName: "Smartphone",
    price: 500,
    quantity: 0,
    isAvailable: true
  };
  
  let product3 = {
    productName: "Headphones",
    price: 150,
    quantity: 2,
    isAvailable: false
  };
  
  let inventory = {
    product1: product1,
    product2: product2,
    product3: product3,

    displayAvailableProducts: function() {
      if (this.product1.isAvailable && this.product1.quantity > 0) {
        console.log(`${this.product1.productName} - $${this.product1.price}, Quantity: ${this.product1.quantity}`);
      }
      if (this.product2.isAvailable && this.product2.quantity > 0) {
        console.log(`${this.product2.productName} - $${this.product2.price}, Quantity: ${this.product2.quantity}`);
      }
      if (this.product3.isAvailable && this.product3.quantity > 0) {
        console.log(`${this.product3.productName} - $${this.product3.price}, Quantity: ${this.product3.quantity}`);
      }
    }
  };

  inventory.displayAvailableProducts();
  
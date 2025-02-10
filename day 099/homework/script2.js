function Car(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;

    this.getCarInfo = function() {
      return `Brand: ${this.brand}, Model: ${this.model}, Year: ${this.year}`;
    };
  }

  let car1 = new Car("Toyota", "Corolla", 2021);
  let car2 = new Car("Ford", "Mustang", 2020);
  let car3 = new Car("Tesla", "Model 3", 2022);
  
  console.log(car1.getCarInfo());
  console.log(car2.getCarInfo());
  console.log(car3.getCarInfo());
  
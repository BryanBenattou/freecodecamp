//Classes: When we have an object with at least one method, we need a blueprint to create objects of that type. 

class Vegetable {
    constructor(name) {
      this.name = name;
    }
  }
  
  const carrot = new Vegetable('carrot');
  console.log(carrot.name); // Should display 'carrot'
  
  const onion = new Vegetable('onion');
  console.log(onion.name); // Should display 'onion'
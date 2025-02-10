console.log(Object.is(25, 25));       
console.log(Object.is(25, "25"));     
console.log(Object.is(NaN, NaN));     
console.log(Object.is(-0, 0));       
console.log(Object.is(0, -0));       

let obj = { name: "Alice", age: 25 };
Object.preventExtensions(obj);

obj.name = "Bob";  
obj.city = "New York";  
console.log(obj);  

let obj1 = { name: "Alice" };
let obj2 = Object.preventExtensions({ name: "Bob" });

console.log(Object.isExtensible(obj1));  
console.log(Object.isExtensible(obj2));  

let target = { name: "Alice" };
let source1 = { age: 25 };
let source2 = { city: "New York" };

let result = Object.assign(target, source1, source2);
console.log(result);  
console.log(target);  

let original = { name: "Alice", age: 25 };
let clone = Object.assign({}, original);
console.log(clone);  
console.log(original === clone);  

let academy = {
    name: "Tech Academy",
    courses: 5,
    socialLink: "www.techacademy.edu",
    reviews: {
      user1: {
        name: "Alice",
        status: "parent",
        review: "Great academy with excellent resources!"
      },
      user2: {
        name: "Bob",
        status: "child",
        review: "Learned a lot, but the content could be more interactive."
      },
      user3: {
        name: "Charlie",
        status: "parent",
        review: "Good teachers, but the structure needs improvement."
      }
    }
  };
  
  // 1. Output the object’s properties and values
  console.log(Object.entries(academy));
  
  // 2. Output the object’s property names
  console.log(Object.keys(academy));
  
  // 3. Output the object’s property values
  console.log(Object.values(academy));
  
  // 4. Check if the object has a specific property
  console.log(academy.hasOwnProperty('socialLink')); // true
  console.log(academy.hasOwnProperty('location')); // false
  
  // 5. Merge the object with a new object containing a "member" property
  let newObject = { member: "Yes" };
  Object.assign(academy, newObject);
  console.log(academy);
  
  // 6. Freeze the object
  Object.freeze(academy);
  
  // 7. Check if the object is frozen
  console.log(Object.isFrozen(academy));  // true
  
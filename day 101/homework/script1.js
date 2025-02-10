let university = {
    name: "Tech University",
    departments: 10,
    website: "www.techuniversity.edu",
    ratings: {
      student1: 4.5,
      student2: 4.0,
      student3: 4.7
    }
  };
  
  console.log(university);
  
  console.log("Has scholarship property:", university.hasOwnProperty('scholarship'));
  
  Object.assign(university, { studentsCount: 5000 });
  console.log(university);
  
  Object.freeze(university);
  university.name = "New University";
  console.log(university);
  
  console.log("Is object frozen:", Object.isFrozen(university));
  
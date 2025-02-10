let sportsClub = {
    clubName: "Victory FC",
    sportType: "Football",
    foundedYear: 1995,
    achievements: {
      title1: "League Champion 2000",
      title2: "Cup Winner 2005",
      title3: "Best Club 2010"
    }
  };
  
  console.log(Object.keys(sportsClub));
  console.log(Object.values(sportsClub));
  
  console.log("Has sponsors property:", sportsClub.hasOwnProperty('sponsors'));
  
  Object.assign(sportsClub, { stadiumCapacity: 50000 });
  console.log(sportsClub);
  
  Object.freeze(sportsClub);
  sportsClub.clubName = "Champions FC";
  console.log(sportsClub);
  
  console.log("Is object frozen:", Object.isFrozen(sportsClub));
  
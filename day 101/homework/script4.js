let cinema = {
    cinemaName: "Cinema Palace",
    moviesCount: 50,
    location: "Downtown",
    movieReviews: {
      user1: 4.2,
      user2: 4.5,
      user3: 4.0
    }
  };
  
  console.log(cinema);
  
  console.log("Has vipSeats property:", cinema.hasOwnProperty('vipSeats'));
  
  Object.assign(cinema, { ticketPrice: 12 });
  console.log(cinema);
  
  Object.freeze(cinema);
  cinema.cinemaName = "New Cinema";
  console.log(cinema);
  
  console.log("Is object frozen:", Object.isFrozen(cinema));
  
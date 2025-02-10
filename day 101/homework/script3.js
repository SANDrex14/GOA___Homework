let hotel = {
    hotelName: "Grand Resort",
    stars: 5,
    location: "Beachfront",
    guestReviews: {
      guest1: 4.8,
      guest2: 4.3,
      guest3: 4.9
    }
  };
  
  console.log(hotel);
  
  console.log("Has spa property:", hotel.hasOwnProperty('spa'));
  
  Object.assign(hotel, { roomsCount: 200 });
  console.log(hotel);
  
  Object.freeze(hotel);
  hotel.hotelName = "New Resort";
  console.log(hotel);
  
  console.log("Is object frozen:", Object.isFrozen(hotel));
  
const ticket = {
    eventName: "Rock Festival",
    eventDate: "2025-06-15",
    price: 50,
    isAvailable: true,
    purchaseTicket() {
      if (this.isAvailable) {
        this.isAvailable = false;
        return `Ticket for ${this.eventName} on ${this.eventDate} has been purchased for $${this.price}.`;
      } else {
        return `Sorry, tickets for ${this.eventName} are sold out.`;
      }
    }
  };
  
  console.log(ticket.purchaseTicket());
  console.log(ticket.purchaseTicket());
  
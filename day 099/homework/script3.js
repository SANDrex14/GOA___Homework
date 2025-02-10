let library = {
    name: "Central Library",
    location: "Downtown",
    books: [
      {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        year: 1960
      },
      {
        title: "1984",
        author: "George Orwell",
        year: 1949
      },
      {
        title: "Moby Dick",
        author: "Herman Melville",
        year: 1851
      }
    ],
  
    listBooks: function() {
      this.books.forEach(function(book) {
        console.log(`This book's name is "${book.title}", written by ${book.author}, published in ${book.year}. You can find it at the ${this.name} located at ${this.location}.`);
      }, this); 
    }
  };
  
  library.listBooks();
  
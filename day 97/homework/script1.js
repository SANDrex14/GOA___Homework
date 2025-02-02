const book = {
    title: "1984",
    author: "George Orwell",
    pages: 328,
    publishYear: 1949,
    getSummary() {
      return `${this.title} by ${this.author}, published in ${this.publishYear}, has ${this.pages} pages.`;
    }
  };
  
  console.log(book.getSummary());
  
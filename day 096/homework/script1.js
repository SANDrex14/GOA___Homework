book = {
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    year: 1925,
    genre: "Novel",
    price: 15.99
};

console.log(book);

console.log(book.title);
console.log(book["author"]);
console.log(book.year);
console.log(book["genre"]);
console.log(book.price);

console.log(`The book "${book.title}" was written by ${book.author} in the year ${book.year}. It falls under the ${book.genre} genre and costs $${book.price}.`);

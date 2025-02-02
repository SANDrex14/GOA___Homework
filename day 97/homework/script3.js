const movie = {
    title: "Inception",
    director: "Christopher Nolan",
    releaseYear: 2010,
    duration: 148,
    getMovieInfo() {
      return `${this.title}, directed by ${this.director}, was released in ${this.releaseYear} and has a duration of ${this.duration} minutes.`;
    }
  };
  
  console.log(movie.getMovieInfo());
  
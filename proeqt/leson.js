// scripts.js

document.getElementById('contact-form').addEventListener('submit', function(event) {
  event.preventDefault(); 

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const message = document.getElementById('message').value;

  if (name && email && message) {
      alert('გმადლობთ, თქვენი შეტყობინება გაიგზავნა!');

  } else {
      alert('გთხოვთ, შეავსოთ ყველა ველი!');
  }
});

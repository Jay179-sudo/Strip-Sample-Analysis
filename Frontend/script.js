document
  .getElementById("submitForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var email = document.getElementById("email").value;
    var image = document.getElementById("image").files[0];

    var formData = new FormData();
    formData.append("email", email);
    formData.append("image", image);

    fetch("http://localhost:1337/v1/home/", {
      method: "POST",
      body: formData,
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        console.log(data);
        // Handle the response from the server as needed
      })
      .catch(function (error) {
        console.error("Error:", error);
      });
  });

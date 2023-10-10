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
        var resultMessage = data.msg;
        var resultDiv = document.getElementById("resultMessage");
        if (!resultDiv) {
          resultDiv = document.createElement("div");
          resultDiv.id = "resultMessage";
          document.body.appendChild(resultDiv);
        }
        resultDiv.innerHTML = resultMessage;

        document.getElementById("submitForm").reset();
      })
      .catch(function (error) {
        console.error("Error:", error);
      });
  });

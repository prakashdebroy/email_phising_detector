console.log("Script loaded successfully.");

document.getElementById("email-form").addEventListener("submit", function (e) {
    e.preventDefault();
    var email_body = document.getElementById("email_body").value;
    
    console.log("Sending email body: ", email_body);  // Log the email body to ensure it's being captured

    var formData = new FormData();
    formData.append('email_body', email_body);

    fetch("/check_email", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Check the response from Flask
        document.getElementById("result").innerHTML = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

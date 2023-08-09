document.addEventListener("DOMContentLoaded", function () {
    console.log("hi");
    const form = document.getElementById("upload-form");
    const message = document.getElementById("message");
    const uploadButton = document.getElementById("upload-btn");

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        console.log("Button clicked!");
        const formData = new FormData(form);

        fetch("http://localhost:5000/upload", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            message.textContent = data.message;
        })
        .catch(error => {
            message.textContent = "Error uploading data.";
            console.error("Error:", error);
        });
    });
});

function checkURL() {
    var url = document.getElementById("urlInput").value;
    fetch("/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: url }),
    })
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("result").textContent = data.result;
    });
}

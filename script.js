async function calculate() {
  const expression = document.getElementById("expression").value;

  try {
    const response = await fetch("http://127.0.0.1:5000/calculate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ expression })
    });

    const data = await response.json();
    document.getElementById("result").innerText = "Result: " + data.result;
  } catch (err) {
    document.getElementById("result").innerText = "Error connecting to server!";
  }
}
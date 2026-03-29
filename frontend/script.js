function predict() {
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      pregnancies: 1,
      glucose: Number(document.getElementById("glucose").value),
      blood_pressure: 70,
      skin_thickness: 20,
      insulin: 80,
      bmi: Number(document.getElementById("bmi").value),
      dpf: 0.5,
      age: Number(document.getElementById("age").value)
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText =
      `${data.prediction} (${data.probability}%)`;
  });
}

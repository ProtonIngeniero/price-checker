function verPrecio(codigo) {
  const pin = document.getElementById("pin").value;

  fetch("/ver_precio", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({codigo, pin})
  })
  .then(r => r.json())
  .then(data => {
    if (data.precio) {
      document.getElementById("bloqueado").style.display = "none";
      document.getElementById("precio").style.display = "block";
      document.getElementById("valor").innerText = "$" + data.precio;

      setTimeout(() => {
        location.reload();
      }, 180000); // 3 minutos
    } else {
      alert("PIN incorrecto");
    }
  });
}

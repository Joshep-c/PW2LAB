document.addEventListener("DOMContentLoaded", function () {
  var ingresoButton = document.getElementById("envioUrl");
  ingresoButton.addEventListener("click", getMeetCode);
});

function getMeetCode() {
  var meetUrlPorDefecto = document.getElementById("meetUrl");

  var meetUrl = meetUrlPorDefecto.value.trim();

  if (extractMeetCode(meetUrl) != null) {
    var meetCode = extractMeetCode(meetUrl);
    document.getElementById("meetCodigo").innerHTML = "Código de la sesión: " + meetCode;
  }
  else {
    document.getElementById("meetCodigo").innerHTML = "No se encontró un código de sesión válido en el URL proporcionado.";
  }

}

function extractMeetCode(url) {
  var urlWithoutProtocol = url.replace(/^(https?:\/\/)?(www\.)?/i, "");

  var meetCodeWithDashes = urlWithoutProtocol.match(/\/([\w-]+)/);

  if (meetCodeWithDashes != null) {
    var meetCode = meetCodeWithDashes[1];
    var meetCodeWithoutDashes = meetCode.replace(/-/g, "");
    return meetCodeWithoutDashes;
  }
  else {
    return null;
  }
}
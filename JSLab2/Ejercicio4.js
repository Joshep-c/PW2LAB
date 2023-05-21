
window.addEventListener("keydown", (e)=>{
  if(e.keyCode === 13){
    ejecucion(e);
  }
});

document.addEventListener("DOMContentLoaded", function () {
  var ingresoButton = document.getElementById("envioUrl");
  ingresoButton.addEventListener("click", recibirUrl);
});

function ejecucion(){
  var ingresoButton = document.getElementById("envioUrl");
  ingresoButton.addEventListener("click", recibirUrl);
}

function recibirUrl() {
  var meetUrlPorDefecto = document.getElementById("meetUrl");

  var urlSinEspacios = meetUrlPorDefecto.value.trim();

  if (extraerCodigo(urlSinEspacios) != null) {
    var meetCode = extraerCodigo(urlSinEspacios);
    document.getElementById("meetCodigo").innerHTML = "Código de la sesión: " + meetCode;
  }
  else {
    document.getElementById("meetCodigo").innerHTML = "ERROR: La url ingresada o el codigo no es valido";
  }

}

function extraerCodigo(url) {
  var urlSinProtocolos = url.replace(/^(https?:\/\/)?/i, "");
  
  if((/^meet\.google\.com\/([\w-]+)$/i).test(urlSinProtocolos)){
    var extraccionCodigo = urlSinProtocolos.match(/\/([\w-]+)/);

    if (extraccionCodigo != null) {
      var codigoConGuiones = extraccionCodigo[1];
      if((/^[a-z]{3}-[a-z]{4}-[a-z]{3}$/).test(codigoConGuiones)){
        var codigo = codigoConGuiones.replace(/-/g, "");
        return codigo;
      }
      else{
        return null;
      }
        
    }
    else {
      return null;
    }
  }
  else{
    return null;
  }
}

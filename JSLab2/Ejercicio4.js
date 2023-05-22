document.getElementById("envioUrl").addEventListener("click", recibirUrl);
document.addEventListener("keyup", ejecucion);

function ejecucion(event){
  const teclaPresionada = event.keyCode;
  if(teclaPresionada === 13){
    recibirUrl();
  }
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
  //Borramos la parte incial de la url, los protocolos
  var urlSinProtocolos = url.replace(/^(https:\/\/)?/i, "");

  //Comprobar mediante una expresión regular que es un link de meet:
  //meet.google.com/... 
  if((/^meet\.google\.com\/([\w-]+)$/i).test(urlSinProtocolos)){
    //Creamos un arreglo donde se guardaran dos componentes:
    // 1. /pdo-fpuo-jta           2. pdo-fpuo-jta
    var extraccionCodigo = urlSinProtocolos.match(/\/([\w-]+)/);
    
    //Verificamos que el arreglo tenga elementos
    if (extraccionCodigo != null) {
      
      //Seleccionamos el elemento 2 del arreglo, pdo-fpuo-jta
      var codigoConGuiones = extraccionCodigo[1];

      //verificamos mediante una expresión regular que se cuenta con un codigo debidamente tratado
      if((/^[a-z]{3}-[a-z]{4}-[a-z]{3}$/).test(codigoConGuiones)){

        //Eliminamos por fin los guiones y lo retornamos
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

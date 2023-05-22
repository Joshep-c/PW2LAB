//Si el evento click se realiza en el botoon al presionarlo la function recibirUtl(), iniciara
document.getElementById("envioUrl").addEventListener("click", recibirUrl);

//Si se decide presionar la tecla enter despues de terminar el ingreso de la url
//Primero se validara en la function ejecucion si la tecla es enter mediante el KeyCode
//Despues, recien se ejecutara recibirUrl().
document.addEventListener("keyup", ejecucion);
function ejecucion(event){
  const teclaPresionada = event.keyCode;

  //Validacion de teclado
  if(teclaPresionada === 13){
    recibirUrl();
  }
}
  

function recibirUrl() {
  //Se recibe el valor tal cual de la cadena ingresada, sea cual sea
  var meetUrlPorDefecto = document.getElementById("meetUrl");

  //Se procede a borrar espacios antes y despues de la cadena, asi como tambien saltos de linea
  var urlSinEspacios = meetUrlPorDefecto.value.trim();

  //Se inicia la function extraerCodigo() con el argumento urlSinEspacios
  //Se usa dicha function tambien para verificar si la url y el codigo dentro de esta cumplen con los estandares
  if (extraerCodigo(urlSinEspacios) != null) {
    //Se obtiene el codigo como tal dentro de la variable meetCode
    var meetCode = extraerCodigo(urlSinEspacios);

    //Se procede a introducir la cadena de texto y el codigo del url encontrado
    document.getElementById("meetCodigo").innerHTML = "Código de la sesión: " + meetCode;
  }
  else {
    //Se lanza un ERROR, si no se han cumplido ninguno de los estandares, url o codigo correcto
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

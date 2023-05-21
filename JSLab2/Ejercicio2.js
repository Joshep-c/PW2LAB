
const invertirTextoEvent = (event) =>{
    //Metodo para prevenir la carga repetida de la pagina y demas funciones primitivas del navegador
    event.preventDefault();

    //recopilacion de informacion por parte del formulario y almacenamos en un arreglo
    const {texto} = event.target;

    //console.log(event.target.texto);
    //agregando el ".value", despues recopila el valor que tengan

    /*
    Otra manera de hacerlo es: 
    const {texto} = event.target
    Y para comprobar su uso:
    console.log(texto.value);
    */
    
    let textInv = texto.value.split("").reverse().join("");
    document.getElementById("entrada").innerHTML = textInv;
}


//funciones, que reciben una cadena para poder cambiar su orden
function invertirCadenaMetodos(text){
    /*
    Metodos usados:
    Split() = devide la cadena y los convierte en un arreglo 
    Reverse() = invertir el arreglo
    Join() = unir los elementos del arreglo en una cadena*/
    return text.split("").reverse().join("");
}

function invertirCadenaFor(text){
    var nuevoText = "";

    /*
    Primero se crea una nueva cadena vacia donde se almacenara la cadena nueva
    Mediante el for, cada iteración ingresa un caracter en la nueva cadena, desde el útimo al primero*/

    for (var i = text.length - 1; i >= 0; i--){
        nuevoText += text[i];
    }

    return nuevoText;
}

const form = document.querySelector("#formulario")

//evento submit, para enviar todo el formulario
//se escucha el evento submit sobre el elemento form
//despues se ejecuta la accion invertirTexto
form.addEventListener('submit', invertirTextoEvent)


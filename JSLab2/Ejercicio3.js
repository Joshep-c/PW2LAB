
//Se crea la fecha el evento
const aqp = new Date(2023, 7, 15);

//Se obtiene la fecha actual
const hoy = new Date();


//Se restan ambas, como el numero de ambas esta dad en milisegundos
//Luego de divirlas entre las  unidades correpondientes de conversion, para dias
//Finalmente se usa el metodo el metodo floor, para redondear al entero minimo del numero
document.getElementById("dias").innerHTML = Math.floor((aqp - hoy) / (1000 * 60 * 60 * 24)) ;

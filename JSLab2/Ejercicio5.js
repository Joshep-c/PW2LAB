let ingreso = document.getElementById("inp");
let cuerpoTab = document.getElementById("tables");
let crearButton = document.getElementById("crearButton");
let cantTables = 0;
let sum = 0;
let comprobanteNum = true;

document.getElementById("crearButton").addEventListener("click", crearTable);
document.getElementById("eliminarButton").addEventListener("click", elim);

function crearTable() {
  if (ingreso.value > 0 && !isNaN(parseInt(ingreso.value))) {

    ingreso.readOnly = true;
    for (let i = 0; i < ingreso.value; i++) {
      var inputTable = document.createElement("input");
      inputTable.id = "table" + (i+1);
      inputTable.type = "text";
      cuerpoTab.appendChild(inputTable);
      cantTables++;
    }

    crearButton.disabled = true;

    var sumarButton = document.createElement("button");
    sumarButton.id = "sumarButton";
    sumarButton.textContent = "SUMAR";
    cuerpoTab.appendChild(sumarButton);
    

    sumarButton.addEventListener("click", function sumar() {
      event.preventDefault();

      for (var j = cantTables; j > 0; j--) {
        var tableIngreso = document.getElementById("table" + j);
        var number = parseInt(tableIngreso.value);

        if ( isNaN(number) ) {
          document.getElementById("resultado").innerHTML = "ERROR: Algún(os) valor(es) no es(son) validos";
          comprobanteNum = false;
          break;
        }
        
        sum += parseInt(tableIngreso.value);
      }

      if(comprobanteNum){
        document.getElementById("resultado").innerHTML = "La suma es: " + sum;
      }

    });

  }
  else {
    document.getElementById("resultado").innerHTML = "ERROR: Número no valido";
  }
}

function elim() {

  for (let i = 1; i <= cantTables; i++) {
    var input = document.getElementById("table" + i);
    input.remove();
  }


  sumarButton.remove();
  crearButton.disabled = false;
  ingreso.value = "";
  resultado.innerText = "";
  ingreso.readOnly = false;
}
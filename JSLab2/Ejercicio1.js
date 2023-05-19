
function obtenerDiaSemana(numDia) {
    const dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
    const fechaActual = new Date();
    const diaNum = fechaActual.getDay();
    return dias[diaNum];
}

const numDia = new Date().getDay();
const textDia = obtenerDiaSemana(numDia);
console.log(textDia);
function paso1apaso2() {

    document.getElementById("primero").className="row d-none";
    document.getElementById("segundo").className="row d-block";




	document.getElementById('nombreCompleto').innerHTML = document.getElementById('name').value + " " + document.getElementById('1st_last_Name').value;
}

function paso2apaso3() {

    document.getElementById("segundo").className="row d-none";
    document.getElementById("tercero").className="row d-block";


	document.getElementById('nombreUsuario1').innerHTML = document.getElementById('username').value;
	document.getElementById('nombreUsuario2').innerHTML = document.getElementById('username').value;
	document.getElementById('nombreUsuario3').innerHTML = document.getElementById('username').value;
}

function paso3apaso4() {

    document.getElementById("tercero").className="row d-none";
    document.getElementById("cuarto").className="row d-block";

}


/////////////////////////////Retroceder///////////////////////////////



function paso2apaso1() {
    document.getElementById("primero").className="row d-block";
    document.getElementById("segundo").className="row d-none";



}

function paso3apaso2() {

    document.getElementById("segundo").className="row d-block";
    document.getElementById("tercero").className="row d-none";


	document.getElementById('nombreUsuario1').innerHTML = document.getElementById('username').value;
	document.getElementById('nombreUsuario2').innerHTML = document.getElementById('username').value;
	document.getElementById('nombreUsuario3').innerHTML = document.getElementById('username').value;
}

function paso4apaso3() {

    document.getElementById("tercero").className="row d-block";
    document.getElementById("cuarto").className="row d-none";


}
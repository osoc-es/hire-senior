function paso1apaso2() {
	document.getElementById('paso1').classList.add("d-none");
	document.getElementById('paso2').classList.remove("d-none");
	document.getElementById('nombreCompleto').innerHTML = document.getElementById('name').value + " " + document.getElementById('1st_last_Name').value;
}

function paso2apaso3() {
	document.getElementById('paso2').classList.add("d-none");
	document.getElementById('paso3').classList.remove("d-none");
	document.getElementById('nombreUsuario1').innerHTML = document.getElementById('username').value;
	document.getElementById('nombreUsuario2').innerHTML = document.getElementById('username').value;
	document.getElementById('nombreUsuario3').innerHTML = document.getElementById('username').value;
}

function paso3apaso4() {
	document.getElementById('paso3').classList.add("d-none");
	document.getElementById('paso4').classList.remove("d-none");
}

function paso4apaso5() {
	document.getElementById('paso4').classList.add("d-none");
	document.getElementById('paso5').classList.remove("d-none");
}

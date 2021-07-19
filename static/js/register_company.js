function pasar1a2(){

    document.getElementById("primero").className="row d-none";
    document.getElementById("segundo").className="row d-block";

    var company_name = document.getElementById("name").value;
    document.getElementById('name_company').innerHTML = company_name;
}

function pasar2a3(){

    document.getElementById("segundo").className="row d-none";
    document.getElementById("tercero").className="row d-block";

}

function pasarPagHOME(){

    //Se redirige a la pagina "HOME"(aun por crear)
}
//////////////////////////////////Retroceder//////////////////////////////////

function volverPagIndex(){

    //Se redirige a la pagina index
}

function pasar2a1(){

    document.getElementById("primero").className="row d-block";
    document.getElementById("segundo").className="row d-none";

}

function pasar3a2(){

    document.getElementById("segundo").className="row d-block";
    document.getElementById("tercero").className="row d-none";

}
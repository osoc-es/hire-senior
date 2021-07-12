function pasaraGeneral(){
    document.getElementById('account-general').className = "tab-pane fade active show";
    document.getElementById('account-change-password').className = "tab-pane fade";
    document.getElementById('account-info').className = "tab-pane fade";
}

function pasaraPassword(){
    document.getElementById('account-general').className = "tab-pane fade";
    document.getElementById('account-change-password').className = "tab-pane fade active show";
    document.getElementById('account-info').className = "tab-pane fade";
}

function pasaraInfo(){
    document.getElementById('account-general').className = "tab-pane fade";
    document.getElementById('account-change-password').className = "tab-pane fade";
    document.getElementById('account-info').className = "tab-pane fade active show";
}

function nuevaContraseña(){
    var oldPassword = document.getElementById('old_password').value;
    var newPassword = document.getElementById('new_password').value;


}
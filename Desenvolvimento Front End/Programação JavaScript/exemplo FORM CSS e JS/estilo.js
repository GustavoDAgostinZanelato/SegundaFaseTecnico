function Enviar() {
    
    var nome  = document.getElementById("nomeid");
    var fone  = document.getElementById("foneid");
    var email = document.getElementById("emailid");

    if (nome.value === "") {
        alert('Campo nome obrigat�rio...');
    }
    
    if (fone.value === "") {
        alert('Campo telefone obrigat�rio...');
    }
    
    if (email.value === "") {
        alert('Campo e-amil obrigat�rio...');
    }

}
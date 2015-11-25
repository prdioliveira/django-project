function btn_confirm_dialog(){
    var r = confirm("Tem certeza que deseja excluir a postagem?");

    if (r == true){
        window.location="/";
    }
    else{
        return false;
    }
}
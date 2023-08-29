
data_pieces.forEach(([key,  value]) => {
    var imagen = document.getElementById(key);
    //console.log()
    imagen.addEventListener("click", function() {
        chess_Match.show_allowed_move(value); 
    }); 
});





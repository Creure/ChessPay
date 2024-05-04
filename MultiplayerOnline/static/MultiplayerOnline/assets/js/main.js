class Chess_Match extends Chess{
    constructor(id, cookie){
        super()
        this.id = id
        this.cookie = cookie
        this.data_pieces.forEach(([key,  value]) => {
            var imagen = document.getElementById(key);
            //console.log()
            imagen.addEventListener("click", function() {
                
                chess_Match.show_allowed_move(value); 
                //console.log(value)
            }); 
        });
    }
}


chess_Match = new Chess_Match(id, cookie);
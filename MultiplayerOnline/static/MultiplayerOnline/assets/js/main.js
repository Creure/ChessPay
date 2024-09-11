class Chess_Match extends Chess{
    constructor(id, cookie ){
        super(id)
        
        this.cookie = cookie
        /*this.data_pieces.forEach(([key,  value]) => {

            var imagen = document.getElementById(key);
            //console.log()
            imagen.addEventListener("click", function() {
                

                chess_Match.ask_for_legal_moves(value, key); 
                //console.log(value)
            }); 
        });*/
    }
}



chess_Match = new Chess_Match(id, cookie);
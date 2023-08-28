
class Chess{

    constructor(){
        this.ChessBoard = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'], //0
            [new pawn('white', 'a2'), new pawn('white', 'b2'), new pawn('white', 'c2'), new pawn('white', 'd2'), new pawn('white', 'e2'), new pawn('white', 'f2'), new pawn('white', 'g2'), new pawn('white', 'h2')],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            [new pawn('black', 'a7'), new pawn('black', 'b7'), new pawn('black', 'c7'), new pawn('black', 'd7'), new pawn('black', 'e7'), new pawn('black', 'f7'), new pawn('black', 'g7'), new pawn('black', 'h7')],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'] //7
          ];

          this.turn = 'white'
          this.pieces_dead_white = []
          this.pieces_dead_black = []

    }

    show_allowed_move(allows_basic_move){ // here we show the allows move in the board
        
    }
}
chess_Match = new Chess()

function gui(box){ // a2  when we are looking in the matriz looking for the information, first the number then the letter (IMPORTANT)
    //selecting with piece will be playing
    console.log(box)
    var row0 = position[box[0]] 
    var row1 = parseInt(box[1]) - 1// convert a2 == 0,1
    var piece = chess_Match.ChessBoard[row1][row0]
    var movements = piece.allows_basic_move() //return allow move that piece has enabled
    // changes the color for that allows move .allow class
    console.log(movements)
    const imgindicator = document.querySelectorAll('img[name="indicator"]');

    if(imgindicator != null){
        imgindicator.forEach(function(imagen) {
            imagen.remove();
        });
    }
    // Itera sobre todas las imágenes y elimínalas
    
         
    movements.forEach(function(movement){
        query = 'div[name="' + movement + '"]'
         box_div = document.querySelector(query);

        
        if(box_div.children.length === 0 ){

            const imgElement = document.createElement('img');
            imgElement.src = "/static/Home/assets/images/pieces/element/indicator.png";
            imgElement.setAttribute('name', 'indicator');
            box_div.appendChild(imgElement);
        }
        else{
            //we needs to verify if there is a piece in that box before to add the indicator PNG  or add another if else      
            
           
        }
    });
}



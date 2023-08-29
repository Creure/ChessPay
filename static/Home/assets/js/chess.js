
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
    clearIndicator(){
        const imgindicator = document.querySelectorAll('img[name="indicator"]');

        if(imgindicator != null){
            imgindicator.forEach(function(imagen) {
                imagen.remove();
            });
        }
    }
    changesturn(){
        if(chess_Match.turn === 'white'){
            chess_Match.turn = 'black' 
        }
        else{
            chess_Match.turn = white
        }
    }
    show_allowed_move(box){ // here we show the allows move in the board
        console.log(box)
        var row0 = position[box[0]] 
        var row1 = parseInt(box[1]) - 1// convert a2 == 0,1
        var piece = chess_Match.ChessBoard[row1][row0]
        var movements = piece.allows_basic_move() //return allow move that piece has enabled
        // changes the color for that allows move .allow class
        //console.log(movements)
        this.clearIndicator()
        // Itera sobre todas las imágenes y elimínalas
        
            
        movements.forEach(function(movement){
            var query = 'div[name="' + movement + '"]'
            var box_div = document.querySelector(query);

            
            if(box_div.children.length === 0 ){

                const imgElement = document.createElement('img');
                imgElement.src = "/static/Home/assets/images/pieces/element/indicator.png";
                imgElement.setAttribute('name', 'indicator');
                imgElement.setAttribute('id', 'move_' + movement);
                box_div.appendChild(imgElement);
                
                imgElement.addEventListener("click", function() {
                    chess_Match.move_the_pieces(piece, movement); 
                }); 

            }
            else{
                //we needs to verify if there is a piece in that box before to add the indicator PNG  or add another if else      
                
                
            }
        });
    }


    move_the_pieces(piece, move){

        //check if move is allowed move
       
        if (piece.allows_basic_move().includes(move)){
            // moving the object in the matrix
            var row0 = position[move[0]] 
            var row1 = parseInt(move[1]) - 1// convert a2 == 0,1

            var position_piece = piece.position
            var piece_row0 = position[position_piece[0]] 
            var piece_row1 = parseInt(position_piece[1]) - 1// convert a2 == 0,1

            var obj = chess_Match.ChessBoard[piece_row1][piece_row0]
            chess_Match.ChessBoard[piece_row1][piece_row0] = '-'
            chess_Match.ChessBoard[row1][row0] = obj
            // updating the location- in the object
            chess_Match.ChessBoard[row1][row0].position = move
            // updating the eve_move
            if (chess_Match.ChessBoard[row1][row0].piece == 'pawn'){
                chess_Match.ChessBoard[row1][row0].eve_move = true
            }
            
            // moving img in the board
            var id_img = chess_Match.ChessBoard[row1][row0].piece + '-' +chess_Match.ChessBoard[row1][row0].row + '-' + chess_Match.ChessBoard[row1][row0].color
            var img = document.querySelector('#' + id_img); // pawn-g-black
            var div_square = document.querySelector('[name="' + position_piece + '"]'); 
            var div_square_moveTo = document.querySelector('[name="' + move + '"]'); 

            if (img && div_square && div_square_moveTo){
                div_square.removeChild(img)
                div_square_moveTo.appendChild(img)
            } else {
                console.log("Alguno de los elementos no se encontró.");
            }

            //updating the location in dict 'img_pieces'
            img_pieces[id_img] = move

            // we needs to remove any img indicator in move box
            this.clearIndicator()

            // changes the turn
            this.changesturn()
        }
        else{
            // retorna error if this else execute is because that move you select isn't available
            console.log('Logic Error!')
        }


    }
}


chess_Match = new Chess()
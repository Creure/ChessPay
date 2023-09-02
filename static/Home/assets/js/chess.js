
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
          this.position = {
            'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7
          };
        
        
        this.id_img_pieces = {
            'pawn-a-white': 'a2','pawn-a-black': 'a7','pawn-b-white': 'b2','pawn-b-black': 'b7','pawn-c-white': 'c2','pawn-c-black': 
            'c7','pawn-d-white': 'd2','pawn-d-black': 'd7','pawn-e-white': 'e2','pawn-e-black': 'e7','pawn-f-white': 'f2','pawn-f-black': 
            'f7','pawn-g-white':  'g2','pawn-g-black': 'g7','pawn-h-white': 'h2', 'pawn-h-black': 'h7'
        
        };
        
        this.data_pieces = Object.entries(this.id_img_pieces);
        

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
        if(this.turn === 'white'){
            this.turn = 'black' 
        }
        else{

            
            this.turn = 'white'
        }
    }

    move_the_pieces(piece, move, movements){

        //check if move is allowed move
        if (movements.includes(move)){
            // moving the object in the matrix
            var row0 = this.position[move[0]] 
            var row1 = parseInt(move[1]) - 1// convert a2 == 0,1

            var position_piece = piece.position
            var piece_row0 = this.position[position_piece[0]] 
            var piece_row1 = parseInt(position_piece[1]) - 1// convert a2 == 0,1

            var obj = this.ChessBoard[piece_row1][piece_row0]
            this.ChessBoard[piece_row1][piece_row0] = '-'
            this.ChessBoard[row1][row0] = obj
            // updating the location- in the object
            
            // updating the eve_move
            if (this.ChessBoard[row1][row0].piece == 'pawn'){
                this.ChessBoard[row1][row0].eve_move = true
            }
            
            // moving img in the board
            var id_img = this.ChessBoard[row1][row0].piece + '-' +this.ChessBoard[row1][row0].row + '-' + this.ChessBoard[row1][row0].color
            var img = document.querySelector('#' + id_img); // pawn-g-black
            var div_square = document.querySelector('[name="' + position_piece + '"]').removeChild(img)
            var div_square_moveTo = document.querySelector('[name="' + move + '"]'); 
            // fixing bugs the img doesn't update the event listener  // 
            img = img.cloneNode(true);
            img.addEventListener("click", function() {
                
                chess_Match.show_allowed_move(move); 
                //console.log(value)
            }); 
            // ending
            if (img && div_square_moveTo){
                
                div_square_moveTo.appendChild(img)
                this.ChessBoard[row1][row0].position = move
            } else {
                console.log("Alguno de los elementos no se encontró.");
            }

            //updating the location in dict 'this.id_img_pieces'
            this.id_img_pieces[id_img] = move

            // we needs to remove any img indicator in move box
            this.clearIndicator()

            // changes the turn
            this.changesturn()

            // update the event listening in the img
            
        }
        else{
            // retorna e(rror if this else execute is because that move you select isn't available
            console.log('Logic Error!')
        }


    }

    show_allowed_move(box){ // here we show the allows move in the board
        
        var row0 = this.position[box[0]];
        var row1 = parseInt(box[1]) - 1// conve'rt a2 == 0,1
        var piece = this.ChessBoard[row1][row0]; // make sure 'piece' is a object 
        var movements = piece.allows_basic_move();
        this.clearIndicator()
        // Itera sobre todas las imágenes y elimínalas
        
            
        movements.forEach(function(movement){
            var query = 'div[name="' + movement + '"]'
            var box_div = document.querySelector(query);

            
            if(box_div.children.length === 0 ){
                // this condition avoid create indicator img object on piece
                const imgElement = document.createElement('img');
                imgElement.src = "/static/Home/assets/images/pieces/element/indicator.png";
                imgElement.setAttribute('name', 'indicator');
                imgElement.setAttribute('id', 'move_' + movement);
                imgElement.setAttribute("draggable","false")
                box_div.appendChild(imgElement);
                
                imgElement.addEventListener("click", function() {
                    chess_Match.move_the_pieces(piece, movement, movements); 
                }); 
                


            }
            else{
                   
                return;
                
                
            }
        });
    }


    
}



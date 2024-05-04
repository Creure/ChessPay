
class Chess{

    constructor(){
        this.ChessBoard = [
            [new Rook('white', 'a1'), new Knight('white','b1'), new Bishop('white', 'c1'), new Queen('white', 'd1'), new King('white', 'e1'), new Bishop('white', 'f1'), new Knight('white','g1'), new Rook('white', 'h1')], //0
            [new pawn('white', 'a2'), new pawn('white', 'b2'), new pawn('white', 'c2'), new pawn('white', 'd2'), new pawn('white', 'e2'), new pawn('white', 'f2'), new pawn('white', 'g2'), new pawn('white', 'h2')],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            [new pawn('black', 'a7'), new pawn('black', 'b7'), new pawn('black', 'c7'), new pawn('black', 'd7'), new pawn('black', 'e7'), new pawn('black', 'f7'), new pawn('black', 'g7'), new pawn('black', 'h7')],
            [new Rook('black', 'a8'), new Knight('black','b8'), new Bishop('black', 'c8'),  new Queen('black', 'd8'), new King('black', 'e8'), new Bishop('black', 'f8'),new Knight('black','g8'), new Rook('black', 'h8')] //7
          ];
        this.id=''

        this.turn = 'white'
        this.pieces_dead_white = []
        this.pieces_dead_black = []
        this.position = {
        'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7
        };
        
        

        if(this.id = 'dc724af18fbdd4e59189f5fe768a5f8311527050d9b8a52c989f6e7f085e8b90'){

            this.id_img_pieces = {
                'pawn-a-white': 'a2','pawn-b-white': 'b2','pawn-c-white': 'c2','pawn-d-white': 'd2',
                'pawn-e-white': 'e2','pawn-f-white': 'f2','pawn-g-white':  'g2', 'pawn-h-white': 'h2',
                'rook-a-white': 'a1', 'rook-h-white':'h1', 'knight-b-white': 'b1','knight-g-white': 'g1',
                'bishop-c-white': 'c1','bishop-f-white': 'f1', 'queen-d-white':'d1', 'king-e-white': 'e1',
            }

        }else if(this.id = '32523caacfbc25d536b7e7ccbc7e3e97baf4b9e38fc43d229de3da54c36e7a4b'){
            this.id_img_pieces = {
                'pawn-a-black': 'a7','pawn-b-black': 'b7','pawn-c-black': 'c7','pawn-d-black': 'd7',
                'pawn-e-black': 'e7','pawn-f-black': 'f7','pawn-g-black':  'g7', 'pawn-h-black': 'h7',
                'rook-a-black': 'a8', 'rook-h-black':'h8', 'knight-b-black': 'b8','knight-g-black': 'g8',
                'bishop-c-black': 'c8','bishop-f-black': 'f8', 'queen-d-black':'d8', 'king-e-black': 'e8'
            }
        }
        this.data_pieces = Object.entries(this.id_img_pieces);

    }
   
    send_data(position, pieceName, piece_color,move,movements,kill,piece){
        
        var data = {
            'type': 'match',
            'position': position,
            'piece_eve_move':piece.eve_move,
            'piece_name': pieceName,
            'piece_color':piece_color,
            'move': move,
            'movements':movements,
            'kill': kill,
            'board':this.ChessBoard,
            'turn': this.turn,
            'pieces_dead_white':this.pieces_dead_white,
            'pieces_dead_black':this.pieces_dead_black,
            'sender': this.cookie
        };
        socket.send(JSON.stringify({ 'data': data}));
        
    }
    
    
    clearIndicator(){
        const imgindicator = document.querySelectorAll('img[name="indicator"]');
        const kill_move_indicator = document.querySelectorAll('.img_piece_alert');
        const killIndicatorImages = document.querySelectorAll('img[name="kill_indicator"]');
        

        if(imgindicator != null){
            imgindicator.forEach(function(imagen) { 
                imagen.remove();
            });
        }

        kill_move_indicator.forEach((elemento) => {
                elemento.classList.remove('img_piece_alert');
        });

       
        killIndicatorImages.forEach(img => {
                const imgClone = img.cloneNode(true); 
                img.parentElement.appendChild(imgClone); 
                img.remove(); 
              });

    }

    changesturn(){
        if(this.turn === 'white'){
            
            this.turn = 'black' 
        }
        else{
            this.turn = 'white'
        }
    }

    

    kill_and_move_the_pieces(piece, move, movements){ // piece is teammate piece //box_div has the div where is enemy piece img
        
        var enemy_piece_rows = changes_location_to_matrix(move)
        var enemy_piece = this.ChessBoard[enemy_piece_rows[1]][enemy_piece_rows[0]]
        if (movements.includes(move)){
            // moving the object in the matrix
            var box_div = document.querySelector('div[name="' + move + '"]');
            
            
            var row0 = this.position[move[0]] 
            var row1 = parseInt(move[1]) - 1// convert a2 == 0,1

            var position_piece = piece.position

            var piece_row0 = this.position[position_piece[0]] 
            var piece_row1 = parseInt(position_piece[1]) - 1// convert a2 == 0,1

            var obj = this.ChessBoard[piece_row1][piece_row0]
            this.ChessBoard[piece_row1][piece_row0] = '-'
            this.ChessBoard[row1][row0] = obj
            // updating the location- in the object
            
            
            // moving img in the board
            var id_img = this.ChessBoard[row1][row0].piece + '-' +this.ChessBoard[row1][row0].row + '-' + this.ChessBoard[row1][row0].color
            var img = document.querySelector('#' + id_img); // pawn-g-black
            try {
                var div_square = document.querySelector('[name="' + position_piece + '"]').removeChild(img)
            }catch (error){
                 // there isn't img
            } // error when there isn't images
            var div_square_moveTo = document.querySelector('[name="' + move + '"]'); 
            // fixing bugs the img doesn't update the event listener  // 
            
            box_div.removeChild(box_div.querySelector('img')); // here deleted all img in this 
            
            img.addEventListener("click", function() {
                
                chess_Match.show_allowed_move(move); 
                //console.log(value)
            }); 
            // ending
            if (img && div_square_moveTo){
                div_square_moveTo.appendChild(img)
                this.ChessBoard[row1][row0].position = move
                if (box_div) {
                    // Busca la imagen dentro del div
                    
                        
                        if(enemy_piece.color == 'black'){
                            this.pieces_dead_black.push(enemy_piece)
                        }else{
                            this.pieces_dead_white.push(enemy_piece)
                        }
                    }
            } else {
                console.log("Alguno de los elementos no se encontró.");
            }

            //updating the location in dict 'this.id_img_pieces'
            this.id_img_pieces[id_img] = move

            // we needs to remove any img indicator in move box
            this.clearIndicator()
            //send the move and information to server before to changes the turn
            this.send_data(position_piece, piece.piece, piece.color,move,movements,true, piece)

            // changes the turn
            this.changesturn()

            

            
        }
        else{
            // retorna e(rror if this else execute is because that move you select isn't available
            console.log('Logic Error!')
        }
    }

    move_the_pieces(piece, move, movements){

        //check if move is allowed move
        console.log('debug:',movements, move)

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
            console.log('ID_IMG: ', id_img)
            
            var img = document.querySelector('#' + id_img); // pawn-g-black
            
            //console.log('position_piece: ', position_piece)
            var div_square = document.querySelector('[name="' + position_piece + '"]').removeChild(img) //removechild returns an error when img doesn't exist or ID is incorrect
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
            //send the move and information to server before to changes the turn
            this.send_data(position_piece, piece.piece, piece.color,move, movements,false, piece)
            // changes the turn
            this.changesturn()
            

            
        }
        


    }

    show_allowed_move(box){ // here we show the allows move in the board
        
        var row0 = this.position[box[0]];
        var row1 = parseInt(box[1]) - 1// conve'rt a2 == 0,1
        var piece = this.ChessBoard[row1][row0]; // make sure 'piece' is a object 
        var movements = piece.allows_basic_move();
        this.clearIndicator()
        // Itera sobre todas las imágenes y elimínalas
        
            
        movements.forEach(function(movement){ //update movement var
            var query = 'div[name="' + movement + '"]'
            var box_div = document.querySelector(query);

            
            if(box_div.children.length === 0 ){
                // this condition avoid create indicator img object on piece
                const imgElement = document.createElement('img');
                imgElement.src = "/static/MultiplayerOnline/assets/images/pieces/element/indicator.png";
                imgElement.setAttribute('name', 'indicator');
                imgElement.setAttribute('id', 'move_' + movement);
                imgElement.setAttribute("draggable","false")
                box_div.appendChild(imgElement);
                
                imgElement.addEventListener("click", function() {
                    chess_Match.move_the_pieces(piece, movement, movements); 
                }); 
                


            }
            else if(box_div.children.length === 1 ){
                
                // create a codicion piece.color != enemy.color
                var enemy_piece = box_div.children[0]
                enemy_piece.classList.add('img_piece_alert')
                enemy_piece.name = 'kill_indicator'
                enemy_piece.addEventListener("click", function() {
                        chess_Match.kill_and_move_the_pieces(piece, movement, movements); 
                        
                    }); 
                
                
            }
        });
    }


    
}



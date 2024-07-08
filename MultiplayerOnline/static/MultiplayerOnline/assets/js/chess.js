
class Chess{

    constructor(id){
        
        this.id=id
        this.chess_board_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        
        
        this.turn = 'white';
        if(this.id == 'white'){

            this.id_img_pieces = {
                'pawn-a-white': 'a2','pawn-b-white': 'b2','pawn-c-white': 'c2','pawn-d-white': 'd2',
                'pawn-e-white': 'e2','pawn-f-white': 'f2','pawn-g-white':  'g2', 'pawn-h-white': 'h2',
                'rook-a-white': 'a1', 'rook-h-white':'h1', 'knight-b-white': 'b1','knight-g-white': 'g1',
                'bishop-c-white': 'c1','bishop-f-white': 'f1', 'queen-d-white':'d1', 'king-e-white': 'e1',
            }

        }else{
            this.id_img_pieces = {
                'pawn-a-black': 'a7','pawn-b-black': 'b7','pawn-c-black': 'c7','pawn-d-black': 'd7',
                'pawn-e-black': 'e7','pawn-f-black': 'f7','pawn-g-black':  'g7', 'pawn-h-black': 'h7',
                'rook-a-black': 'a8', 'rook-h-black':'h8', 'knight-b-black': 'b8','knight-g-black': 'g8',
                'bishop-c-black': 'c8','bishop-f-black': 'f8', 'queen-d-black':'d8', 'king-e-black': 'e8'
            }
        }
        this.data_pieces = Object.entries(this.id_img_pieces);

    }

    update_chessboard(){


    
        const images = document.querySelectorAll('.square img');
        images.forEach(image => {
            image.remove();
        });


        var id = {
            'rook_black': ['rook-a-black', 'rook-h-black'],
            'knight_black': ['knight-b-black', 'knight-g-black'],
            'bishop_black': ['bishop-c-black', 'bishop-f-black'],
            'queen_black': ['queen-d-black'],
            'king_black': ['king-e-black'],
            'pawn_black': ['pawn-a-black', 'pawn-b-black', 'pawn-c-black', 'pawn-d-black', 'pawn-e-black', 'pawn-f-black', 'pawn-g-black', 'pawn-h-black'],
            'rook_white': ['rook-a-white', 'rook-h-white'],
            'knight_white': ['knight-b-white', 'knight-g-white'],
            'bishop_white': ['bishop-c-white', 'bishop-f-white'],
            'queen_white': ['queen-d-white'],
            'king_white': ['king-e-white'],
            'pawn_white': ['pawn-a-white', 'pawn-b-white', 'pawn-c-white', 'pawn-d-white', 'pawn-e-white', 'pawn-f-white', 'pawn-g-white', 'pawn-h-white']
        }
        
        const piece_img_src = {
                'rook_black' : "/static/MultiplayerOnline/assets/images/pieces/black/rook.png", 
                'knight_black' :"/static/MultiplayerOnline/assets/images/pieces/black/knight.png", 
                'bishop_black' : "/static/MultiplayerOnline/assets/images/pieces/black/bishop.png" , 
                'queen_black' : "/static/MultiplayerOnline/assets/images/pieces/black/queen.png", 
                'king_black' :"/static/MultiplayerOnline/assets/images/pieces/black/king.png" , 
                'pawn_black' :"/static/MultiplayerOnline/assets/images/pieces/black/pawn.png" , 
                'rook_white' : "/static/MultiplayerOnline/assets/images/pieces/white/rook.png",
                'knight_white' : "/static/MultiplayerOnline/assets/images/pieces/white/knight.png" ,
                'bishop_white' : "/static/MultiplayerOnline/assets/images/pieces/white/bishop.png",
                'queen_white' : "/static/MultiplayerOnline/assets/images/pieces/white/queen.png",
                'king_white' : "/static/MultiplayerOnline/assets/images/pieces/white/king.png" ,
                'pawn_white' : "/static/MultiplayerOnline/assets/images/pieces/white/pawn.png"
        }

    
    
    
        const pieceMap = {
            'r': 'rook-black', 'n': 'knight-black', 'b': 'bishop-black', 'q': 'queen-black', 'k': 'king-black', 'p': 'pawn-black',
            'R': 'rook-white', 'N': 'knight-white', 'B': 'bishop-white', 'Q': 'queen-white', 'K': 'king-white', 'P': 'pawn-white'
        };
        
        

        const rows = this.chess_board_fen.split('/');
        const board = [];
        const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
        let n = 0;
        
        rows.forEach((row, rowIndex) => {
            let colIndex = 0;
            
            for (let char of row) {
                if (isNaN(char)) {
                    const piece = pieceMap[char];
                    const file = files[colIndex];
                    const rank = 8 - rowIndex;
                    const position = `${file}${rank}`;
                    if(piece  != undefined){
                        board.push([piece, position]);
                        
                    }
                    
                    
                    colIndex += 1;
                } else {
                    colIndex += parseInt(char);
                }
            }
        });
        
        board.forEach(piece => {
            //...
            
            if(piece[0].includes("black")){
                var color = 'black';
            }else{
                var color = 'white'
            }
            var id_img = id[piece[0].split('-')[0].toLowerCase() + '_' +color][0]
            
            var box_div = document.querySelector('div[name="' + piece[1]  + '"]');
            
            const imgElement = document.createElement('img');
            imgElement.src = piece_img_src[piece[0].split('-')[0].toLowerCase()+ '_'+ color]
            imgElement.setAttribute('id', id_img ); //ID "pawn-b-white"
            imgElement.setAttribute("draggable","false")
            if(box_div){
                box_div.appendChild(imgElement);
            }
            

            
            imgElement.addEventListener("click", function() {
                chess_Match.ask_for_legal_moves(piece[1], id_img); 
            });              

            id[piece[0].split('-')[0].toLowerCase() + '_' +color].splice(id[piece[0].split('-')[0].toLowerCase() + '_' +color].indexOf(id_img), 1);
            
        });


        
    
    


        


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


    ask_for_legal_moves(box,img_id){
        socket.send(JSON.stringify({'data':{'type': 'legal_moves', 'position':box, 'img_id': img_id}}));

    }

    send_the_selected_move(move, position, img_id){
        socket.send(JSON.stringify({'data':{'type': 'do_the_move', 'move':move, 'position': position, 'img_id':img_id}}));
        this.clearIndicator()

    }




    move_the_pieces(move, position, img_id, remove){
        
        var divA2 = document.querySelector('div[name="'+move+'"]');
        var img = divA2.querySelector('img');
        if (img) {
            img.parentNode.removeChild(img);
        }

        
        
        var img = document.querySelector('#' + img_id); // pawn-g-black
        
        //console.log('position_piece: ', position_piece)
        var div_square = document.querySelector('[name="' + position + '"]').removeChild(img) //removechild returns an error when img doesn't exist or ID is incorrect
        var div_square_moveTo = document.querySelector('[name="' + move + '"]'); 
        
        // fixing bugs the img doesn't update the event listener  // 
        img = img.cloneNode(true);
        img.addEventListener("click", function() {
            
            chess_Match.ask_for_legal_moves(move, img_id); 
            //console.log(value)
        }); 
        // ending
        if (img && div_square_moveTo){
            
            div_square_moveTo.appendChild(img)
            
        } else {
            console.log("Alguno de los elementos no se encontró.");
        }

        //updating the location in dict 'this.id_img_pieces'
        

        // we needs to remove any img indicator in move box
        this.clearIndicator()

        
        

        
    
    


    }

   

    show_allowed_move(movements, position, img_id){ // here we show the allows move in the board
        
        this.clearIndicator()
        console.log(this.turn + ' // ' + this.id)
        if(this.turn !== this.id){
            return null
        }        
        movements.forEach(function(movement){ //update movement var
            var move  = movement.substring(movement.length - 2);
            var query = 'div[name="' + move + '"]'
            var box_div = document.querySelector(query);
            
            
            if(box_div.children.length === 0 ){
                // this condition avoid create indicator img object on piece
                const imgElement = document.createElement('img');
                imgElement.src = "/static/MultiplayerOnline/assets/images/pieces/element/indicator.png";
                imgElement.setAttribute('name', 'indicator');
                imgElement.setAttribute('id', 'move_' + move);
                imgElement.setAttribute("draggable","false")
                box_div.appendChild(imgElement);
                
                imgElement.addEventListener("click", function() {
                    chess_Match.send_the_selected_move(movement, position, img_id); 
                }); 

            

            }
            else if(box_div.children.length === 1 ){
                
                // create a codicion piece.color != enemy.color
                var enemy_piece = box_div.children[0]
                enemy_piece.classList.add('img_piece_alert')
                enemy_piece.name = 'kill_indicator'
                enemy_piece.addEventListener("click", function() {
                        chess_Match.send_the_selected_move(movement, position, img_id); 
                        
                    }); 
                
                
            }
        });
    }

    check_mate(){
        alert('CHECK MATE!!')
    }
    
}



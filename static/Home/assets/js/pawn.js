
class pawn{

    constructor(color, position) {
        this.color = color;
        this.position = position; //example a2
        this.eve_move = false;
        this.row = position[0];
        this.piece = 'pawn'
       
      }

    allows_basic_move(){
        // A2
        // allow move 
        //console.log(ChessBoard)
        if(this.position[1] >= 8 || this.position[1] === 1){
            return []
            
        }
        var allows_move = []
        var rows = 'abcdefgh'
        var kill_move = []
        var letters, move
        var color = this.color
        if(color === 'white'){
            var new_position = parseInt(this.position[1]) + 1 
            var  new_position = this.position[0] + new_position.toString();
            allows_move.push(new_position)
            // add 2 step can do when ain't move
            if (this.eve_move === false){
                new_position = parseInt(this.position[1]) + 2 
                new_position = this.position[0] + new_position.toString();
                allows_move.push(new_position)
            }
            
            

        
        }
        else if (color === 'black'){
            var new_position = parseInt(this.position[1]) - 1 
            var  new_position = this.position[0] + new_position.toString();
            allows_move.push(new_position)
            // add 2 step can do when ain't move
            if (this.eve_move === false){
                new_position = parseInt(this.position[1]) - 2 
                new_position = this.position[0] + new_position.toString();
                allows_move.push(new_position)

            }

           
        }
        //We needs to check that new_position has a piece on it var
        allows_move.forEach(function(move){
            
            var row = changes_location_to_matrix(move)

          
            var piece = chess_Match.ChessBoard[row[1]][row[0]]
            if ( piece instanceof Object){
                // remove that
                
                allows_move = []
            }
        });
        

        // kill move 
        
        if(color === 'white'){
            if(this.position[0] === 'a'){ 
                letters = rows[rows.indexOf(this.position[0]) + 1] // example position = a3
                move = letters + (parseInt(this.position[1]) + 1)  // b4
                kill_move.push(move)

            }else if (this.position[0] === 'h'){
                letters = rows[rows.indexOf(this.position[0]) - 1] // example position = h3
                move = letters + (parseInt(this.position[1]) + 1)  // g4
                kill_move.push(move)
            }else{
                letters = rows[rows.indexOf(this.position[0]) - 1] // example position = h3
                move = letters + (parseInt(this.position[1]) + 1)  // g4
                kill_move.push(move)

                letters = rows[rows.indexOf(this.position[0]) + 1] // example position = a3
                move = letters + (parseInt(this.position[1]) + 1)  // b4
                kill_move.push(move)
            }

        }

        else if(color == black){
            // we needs to add the logic kill move the black piece
        }
        
        // check in the board if there is a enemy piece in those location
        kill_move.forEach(function(move){
            
            var row = changes_location_to_matrix(move)

          
            var piece = chess_Match.ChessBoard[row[1]][row[0]]
            
            
            if ( piece instanceof Object &&  piece.color != color){
                // remove that
                
                allows_move.push(move)
            }
        });

        return  allows_move // ['a3', 'a4]
        
            
         

    
    }
}

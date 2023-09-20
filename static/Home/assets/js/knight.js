
class Knight{

    constructor(color, position) {
        this.color = color;
        this.position = position; //example a2
        this.eve_move = false;
        this.row = position[0];
        this.piece = 'knight'

    }

    allows_basic_move(){

        var position = this.position
        var letter_rows = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		var allow_move = []
        var color = this.color
        const RelativeMove = [
            [-2, -1], [-2, 1],
            [-1, -2], [-1, 2],
            [1, -2], [1, 2],
            [2, -1], [2, 1]
        ];
        
        RelativeMove.forEach(function(move) {
            var rows = [position[0], parseInt(position[1]) ]
            var row_0 = parseInt(letter_rows.indexOf(rows[0]) + move[0])
            var row_1 = move[1] + rows[1]

            if(row_0 <= 8 && row_0 >= 1 &&  row_1 <= 8 && row_1 >= 1  ){
                var movement_rows = letter_rows[row_0] + row_1
                var move_rows = changes_location_to_matrix(movement_rows)
                var enemy_piece = chess_Match.ChessBoard[move_rows[1]][move_rows[0]]

                if(enemy_piece instanceof Object ){
                    if(enemy_piece.color != color){
                        allow_move.push(movement_rows)
                    }
                    
                }else{
                    allow_move.push(movement_rows)
                }
                
            }
        
        }); 

        return allow_move

    }

       
}

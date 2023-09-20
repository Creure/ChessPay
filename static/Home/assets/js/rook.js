
class Rook{

		constructor(color, position) {
			this.color = color;
			this.position = position; //example a2
			this.eve_move = false;
			this.row = position[0];
			this.piece = 'rook'
		}

	allows_basic_move () { // 
		var color = this.color
		
		var position = this.position
		var allow_move = []
		var letter_rows = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

		for(var i = parseInt(position[1]) + 1 ; i <= 8; i++ ){ // position = 'a2'
			var move = position[0] + i
			var rows = changes_location_to_matrix(move)
			var enemy_piece = chess_Match.ChessBoard[rows[1]][rows[0]]
			
			
			
			if(enemy_piece instanceof Object ){
				if(enemy_piece.color != color){
					allow_move.push(move)
				}
				break;
			}else{
				allow_move.push(move)
			}

		}
		

		for(var i = parseInt(position[1]) - 1 ; i >= 1; i-- ){ // position = 'a2'
			var move = position[0] + i
			var rows = changes_location_to_matrix(move)
			var enemy_piece = chess_Match.ChessBoard[rows[1]][rows[0]]
			
			
			
			if(enemy_piece instanceof Object ){
				if(enemy_piece.color != color){
					allow_move.push(move)
				}
				break;
			}else{
				allow_move.push(move)
			}
		}
		



		for(var i = parseInt(letter_rows.indexOf(position[0])) + 1 ; i <= 8; i++ ){ // position = 'a2'
			
			var move =  letter_rows[i]  + position[1]
			
			var rows = changes_location_to_matrix(move)
		
			var enemy_piece = chess_Match.ChessBoard[rows[1]][rows[0]]
			
			
			if(enemy_piece instanceof Object ){
				if(enemy_piece.color != color){
					allow_move.push(move)
				}
				break;
			}else{
				allow_move.push(move)
			}
		}
		

		
		for(var i = parseInt(letter_rows.indexOf(position[0])) - 1 ; i >= 1; i-- ){ // position = 'a2'
			
			var move =  letter_rows[i]  + position[1]
			
			var rows = changes_location_to_matrix(move)
		
			var enemy_piece = chess_Match.ChessBoard[rows[1]][rows[0]]
			
			
			if(enemy_piece instanceof Object ){
				if(enemy_piece.color != color){
					allow_move.push(move)
				}
				break;
			}else{
				allow_move.push(move)
			}
		}
		
	

		

		return allow_move

}


}

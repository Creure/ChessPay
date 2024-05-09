
class King{

	constructor(color, position) {
		this.color = color;
		this.position = position; //example a2
		this.eve_move = false;
		this.row = position[0];
		this.piece = 'king'

	}
	
	allows_basic_move(){
		var position = this.position
	
		const column = position[0].toLowerCase().charCodeAt(0) - 97; // Convert the letter to column value (0-7)
		const row = parseInt(position[1]) - 1; // Convert the number to row value (0-7)
	   
		const allow_move = [];
		var color = this.color

		if(color != chess_Match.turn){
			return []
		}

		for (let deltaX = -1; deltaX <= 1; deltaX++) {
			for (let deltaY = -1; deltaY <= 1; deltaY++) {
				var move = String.fromCharCode(97 + column + deltaX) + (row + deltaY + 1)
				if(move != position){
					if (column + deltaX >= 0 && column + deltaX <= 7 && row + deltaY >= 0 && row + deltaY <= 7) {
					// Add the valid move to the list of available moves
						
						var rows = changes_location_to_matrix(move)
						var enemy_piece = chess_Match.ChessBoard[rows[1]][rows[0]]
						
						
						if(enemy_piece instanceof Object ){
							if(enemy_piece.color != color){
								allow_move.push(move)
							}
							
							
						}else{
							allow_move.push(move)
						}
						
				  	}
			 	}
			 
		   	}
		}
		 
		return allow_move;
		
	}


}

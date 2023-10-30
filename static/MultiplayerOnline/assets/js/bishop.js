
class Bishop{

	constructor(color, position) {
		this.color = color;
		this.position = position; //example a2
		this.eve_move = false;
		this.row = position[0];
		this.piece = 'bishop'
		

	}
	

	allows_basic_move(){
		var position = this.position
		const column = this.position[0].toLowerCase().charCodeAt(0) - 'a'.charCodeAt(0); // Get the column index (0-7)
		const row = parseInt(this.position[1]) - 1; // Get the row index (0-7)
		var color = this.color
		const allow_move = [];
		
		if(color != chess_Match.turn){
			return []
		}
		
		for (let i = 1; i <= 7; i++) {
			const newColumn = column + i;
			const newRow = row - i;
			if (newColumn >= 0 && newColumn <= 7 && newRow >= 0 && newRow <= 7) {
				var move = String.fromCharCode('a'.charCodeAt(0) + newColumn) + (newRow + 1)
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



				
			} else {
				break;
			}
		}
		
		
		for (let i = 1; i <= 7; i++) {
			const newColumn = column - i;
			const newRow = row - i;
			if (newColumn >= 0 && newColumn <= 7 && newRow >= 0 && newRow <= 7) {
				var move = String.fromCharCode('a'.charCodeAt(0) + newColumn) + (newRow + 1)
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
				

			} else {
				break;
			}
		}
		
		
		for (let i = 1; i <= 7; i++) {
			const newColumn = column + i;
			const newRow = row + i;
			if (newColumn >= 0 && newColumn <= 7 && newRow >= 0 && newRow <= 7) {
				var move = String.fromCharCode('a'.charCodeAt(0) + newColumn) + (newRow + 1)
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

			} else {
				break;
			}
		}
		
		
		for (let i = 1; i <= 7; i++) {
			const newColumn = column - i;
			const newRow = row + i;
			if (newColumn >= 0 && newColumn <= 7 && newRow >= 0 && newRow <= 7) {
				var move = String.fromCharCode('a'.charCodeAt(0) + newColumn) + (newRow + 1)
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

			} else {
				break;
			}
		}
		
		return allow_move;
		
	}

       
}
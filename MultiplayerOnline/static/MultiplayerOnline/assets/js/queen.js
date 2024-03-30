
class Queen {

    constructor(color, position) {
        
        this.color = color;
        this.position = position; //example a2
        this.eve_move = false;
        this.row = position[0];
        this.piece = 'queen'
		this.code_queen = '1a57b84'

    }

	

    allows_basic_move(){
        var color = this.color
		const column = this.position[0].toLowerCase().charCodeAt(0) - 'a'.charCodeAt(0); // Get the column index (0-7)
		const row = parseInt(this.position[1]) - 1;
		var position = this.position
		var allow_move = []
		var letter_rows = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

		if(color != chess_Match.turn){
			return []
		}

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
		
        return allow_move
    }

       
}

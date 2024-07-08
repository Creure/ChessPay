
// websocket.js
class Piece{

	constructor(color, position, eve_move,  piece) {
		this.color = color;
		this.position = position; //example a2
		this.even_move = eve_move
		this.row = position[0];
		this.piece = ''

	}

}

const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';

// Construye la URL del WebSocket utilizando el host de la página actual
const socketUrl = `${protocol}//${window.location.host}/ws/Room/`; 

socket = new WebSocket(socketUrl);

socket.onopen = function(event) {
    console.log('WebSocket connection opened:', event);
    socket.send(JSON.stringify({ 'data': {'sender':chess_Match.cookie, 'type':'_init__'}}));
    

};

socket.onmessage = function(event) {
    
    globalThis.eventData = JSON.parse(event.data);
    chess_Match.turn = eventData['turn']
    if(eventData['message'] ==  'updated_chessboard'){
        chess_Match.chess_board_fen = eventData['chessboard']
        chess_Match.turn = eventData['turn']
        chess_Match.update_chessboard()
    }

    if(eventData['message'] == 'OK'){
        console.log('connected');
        
        return true
    }
    if(eventData['type'] == 'legal_moves' ){
        chess_Match.show_allowed_move(eventData['legal_moves'], eventData['position'], eventData['img_id'])
        

    }

    if(eventData['type'] == 'updated'){
        chess_Match.move_the_pieces(eventData['move'], eventData['position'], eventData['img_id'])
    }
    
    if(eventData['message'] == 'checkmate'){
        window.location.href = '/result';
    }
    

    console.log(eventData)
    
};

socket.onclose = function(event) {
    console.log('WebSocket connection closed:', event);

    
};

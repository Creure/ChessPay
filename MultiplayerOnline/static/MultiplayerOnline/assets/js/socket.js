
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
socket = new WebSocket('ws://localhost:8000/ws/Room/');

socket.onopen = function(event) {
    console.log('WebSocket connection opened:', event);
    socket.send(JSON.stringify({ 'data': {'sender':chess_Match.cookie, 'type':'_init__'}}));
    

};

socket.onmessage = function(event) {
    
    globalThis.eventData = JSON.parse(event.data);
    
    
    if(eventData['message'] == 'OK'){
        console.log('connected');
        
        return true
    }
    if(eventData['type'] == 'legal_moves'){
        chess_Match.show_allowed_move(eventData['legal_moves'], eventData['position'], eventData['img_id'])
        

    }

    if(eventData['type'] == 'updated'){
        chess_Match.move_the_pieces(eventData['move'], eventData['position'], eventData['img_id'])
    }
    
    if(eventData['message'] != ''){
        window.location.href = '/result';
    }


    console.log(eventData)
    
};

socket.onclose = function(event) {
    console.log('WebSocket connection closed:', event);

    
};

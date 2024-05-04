
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
    socket.send(JSON.stringify({ 'data': {'sender':'cookie', 'data':'_init__'}}));
    

};

socket.onmessage = function(event) {
    
    globalThis.eventData = JSON.parse(event.data);
    
    
    if(eventData['message'] == 'OK'){
        console.log('connected');
        
        return true
    }
    
    if (eventData['message']['response'] == id){

        if(eventData['message']['type'] == 'match'){
        var color = eventData.message.piece_color;
        var position = eventData.message.position;
        var eve_move = eventData.message.eve_move;
        var piece = eventData.message.piece_name;


        var piece = new Piece(color, position, eve_move, piece)

        
        if(eventData['message']['kill'] == true){
            chess_Match.kill_and_move_the_pieces(piece, eventData['message']["move"], eventData['message']["movements"])
            
        }else{
            chess_Match.move_the_pieces(piece, eventData['message']["move"], eventData['message']["movements"])
        }
        

        }
    }
    
};

socket.onclose = function(event) {
    console.log('WebSocket connection closed:', event);

    
};

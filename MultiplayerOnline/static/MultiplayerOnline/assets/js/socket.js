
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
    document.getElementById('online-icon-black').classList.remove('hidden')
    document.getElementById('online-icon-white').classList.remove('hidden')
    document.getElementById('offline-icon-black').classList.add('hidden')
    document.getElementById('offline-icon-white').classList.add('hidden')
    
};

socket.onmessage = function(event) {
    
    globalThis.eventData = JSON.parse(event.data);
    

    console.log(eventData)
    switch (eventData['type']) {
        case 'player_status':
            chess_Match.displayPlayersStatus(eventData['status_player_white'], eventData['status_player_white'])
            break;
        case 'updated_chessboard':
            
            chess_Match.chess_board_fen = eventData['chessboard']
            chess_Match.turn = eventData['turn']
            chess_Match.update_chessboard(eventData['chessboard'])
            console.log()
        
            break;
 
        case 'legal_moves':
            chess_Match.show_allowed_move(eventData['legal_moves'], eventData['position'], eventData['img_id'], eventData['message'])
            break;

        case '__init__':
            chess_Match.displayPlayersNames(eventData['username_white'], eventData['username_black'])
            
            chess_Match.turn = eventData['turn']
           
            break;  
        
        case 'updated':
            chess_Match.chess_board_fen = eventData['chessboard']
            chess_Match.update_chessboard(eventData['chessboard'])
            chess_Match.turn = eventData['turn']
            break;        
            
        case 'timer_update':
            chess_Match.updateTimers(eventData['white_timer'], eventData['black_timer'])    
            break;

        case 'pieces_capture_update':
            const pieces_capture_dashboard_white = document.getElementById('pieces_capture_dashboard_white')
            const pieces_capture_dashboard_black = document.getElementById('pieces_capture_dashboard_black')

            pieces_capture_dashboard_white.innerText = eventData['captured_black']
            pieces_capture_dashboard_black.innerText = eventData['captured_white']
            break;
       
    }

    
    
    switch (eventData['message']) {
        case 'checkmate':
            window.location.href = "/result/" + eventData['id']

            break;
        case 'check':
            chess_Match.check_indicator(eventData['turn'], eventData['king_position'])
            break;
        
            
      
        
    }

};

socket.onclose = function(event) {
    console.log('WebSocket connection closed:', event);

    document.getElementById('online-icon-black').classList.add('hidden')
    document.getElementById('online-icon-white').classList.add('hidden')
    document.getElementById('offline-icon-black').classList.remove('hidden')
    document.getElementById('offline-icon-white').classList.remove('hidden')

    
};

// websocket.js
var socket = new WebSocket('ws://localhost:8000/ws/Room/');

socket.onopen = function(event) {
    console.log('WebSocket connection opened:', event);
    socket.send(JSON.stringify({ 'data': 'Hello, server!' }));
};

socket.onmessage = function(event) {
    console.log('Message from server:', event.data);
};

socket.onclose = function(event) {
    console.log('WebSocket connection closed:', event);

    
};

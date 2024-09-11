document.getElementById('toggleButton').addEventListener('click', function() {
    var menu = document.getElementById('formContainer');
    var overlay = document.getElementById('overlay');
    menu.classList.toggle('hidden');
    overlay.classList.toggle('inset-0');
    overlay.classList.toggle('bg-opacity-50');
});

document.getElementById('closeButton').addEventListener('click', function() {
    var menu = document.getElementById('formContainer');
    menu.classList.toggle('hidden');
    var overlay = document.getElementById('overlay');
    menu.classList.toggle('hidden');
    overlay.classList.toggle('inset-0');
    overlay.classList.toggle('bg-opacity-50');
});


 // Seleccionar los elementos
 const whiteKing = document.getElementById('whiteKing');
 const blackKing = document.getElementById('blackKing');

 // Variable global para almacenar la selección
 let selectedPiece = 'white';

 // Función para manejar la selección de la pieza
 function handleSelection(selectedElement, pieceName) {
     // Remover la clase bg-indigo-600 de ambos elementos
     whiteKing.classList.remove('bg-indigo-600');
     blackKing.classList.remove('bg-indigo-600');

     // Agregar la clase bg-indigo-600 al elemento seleccionado
     selectedElement.classList.add('bg-indigo-600');

     // Actualizar la variable con el nombre de la pieza seleccionada
     selectedPiece = pieceName;
     console.log(`Pieza seleccionada: ${selectedPiece}`);
 }

 // Agregar los eventos de click
 whiteKing.addEventListener('click', () => handleSelection(whiteKing, 'whiteKing'));
 blackKing.addEventListener('click', () => handleSelection(blackKing, 'blackKing'));

 // Manejar la selección del monto de la apuesta y hacer el request
 document.getElementById('createlobby').addEventListener('click', function() {
     const betAmountSelect = document.getElementById('betAmount');
     const selectedAmount = betAmountSelect.value;
     const timer = document.getElementById('timer');
     const timerSelected = timer    .value;

     if (selectedPiece) {
         // Construir la URL para el request GET
         const url = '/create/match/' + selectedAmount +'/'+selectedPiece +'/'+timerSelected;

         // Realizar el request GET
        fetch(url)
             .then(response => response.json())
             .then(data => {
                 // Redireccionar a la página del juego
                 const matchId = data.id;
                 console.log(matchId)
                 window.location.href = `/chess/${matchId}`;
             })
             .catch(error => {
                 console.error('Error:', error);
             });
     } else {
         alert("Por favor selecciona una pieza antes de continuar.");
     }
 });
class Chess{

    constructor(){
        this.ChessBoard = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            [new pawn('white', 'a7'), new pawn('white', 'b7'), new pawn('white', 'c7'), new pawn('white', 'd7'), new pawn('white', 'e7'), new pawn('white', 'f7'), new pawn('white', 'g7'), new pawn('white', 'h7')],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            [new pawn('black', 'a2'), new pawn('black', 'b2'), new pawn('black', 'c2'), new pawn('black', 'd2'), new pawn('black', 'e2'), new pawn('black', 'f2'), new pawn('black', 'g2'), new pawn('black', 'h2')],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
          ];
    }

    
}



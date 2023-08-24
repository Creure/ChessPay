class pawn{

    constructor(color, position) {
        this.color = color;
        this.position = position;
        this.eve_move = False

      }

    allows_basic_move(){
        // A2
        // allow move
        allows_move = []
        new_position = parseInt(this.position[1]) + 1 
        new_position = this.position[0] + new_position.toString();

        //We needs to check that new_position has a piece on it
        if(false){

        }

        return [new_position]
    }
}

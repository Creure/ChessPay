
class pawn{

    constructor(color, position) {
        this.color = color;
        this.position = position; //example a2
        this.eve_move = false;
        this.row = position[0];
        this.piece = 'pawn'

      }

    allows_basic_move(){
        // A2
        // allow move 
        var allows_move = []

        if(this.color == 'white'){
            var new_position = parseInt(this.position[1]) + 1 
            var  new_position = this.position[0] + new_position.toString();
            allows_move.push(new_position)
            // add 2 step can do when ain't move
            if (this.eve_move == false){
                new_position = parseInt(this.position[1]) + 2 
                new_position = this.position[0] + new_position.toString();
                allows_move.push(new_position)
            }
            //We needs to check that new_position has a piece on it
            if(false){

            }

            return  allows_move // ['a3', 'a4]
        }
        else if (this.color == 'black'){
            var new_position = parseInt(this.position[1]) - 1 
            var  new_position = this.position[0] + new_position.toString();
            allows_move.push(new_position)
            // add 2 step can do when ain't move
            if (this.eve_move == false){
                new_position = parseInt(this.position[1]) - 2 
                new_position = this.position[0] + new_position.toString();
                allows_move.push(new_position)

            }
            //We needs to check that new_position has a piece on it
            if(false){

            }

            return  allows_move // ['a3', 'a4]
            
        }

    
    }
}

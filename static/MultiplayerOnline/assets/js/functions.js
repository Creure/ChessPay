function changes_location_to_matrix(move){
    position = {
        'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,'f': 5,'g': 6,'h': 7
      };
    var row0 = position[move[0]] 
    var row1 = parseInt(move[1]) - 1// convert a2 == 0,1

    return [row0, row1]
}

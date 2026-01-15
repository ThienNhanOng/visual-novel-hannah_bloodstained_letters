init python:
    import random
    
    #search empty spot base on center pivot
    def OPieceFallback():
        pivot = 4  #pivot choice
        #check left starting at the pivot
        for i in range(pivot, -1, -1): #range(start, stop, step)
            if TttBoard[i] is None:
                to_index = i
                break
        else:
            #Check right
            for i in range(pivot + 1, 9, + 1): #range(start, stop, step)
                if TttBoard[i] is None:
                    to_index = i
                    break
        # Make sure to_index was found
        if 'to_index' not in locals():
            return  # or handle no moves possible

        #Place new piece if less than 3 pieces
        if len(OPieces) < 3:
            placePiece(to_index)
        else:
            #move existing piece (oldest piece)
            from_index = OPieces[0]
            TttSelectedPiece = from_index
            move(to_index)
    
    def aiMove():
    
        if TttState == TTTState.placement:
            #Check through all cells to see if legal play can be made
            for i in range(9):
                #if cell is empty the ai think of a move to play
                if TttBoard[i] is None:
                    TttBoard[i] = tttAI
                    #after simulating a move, check for win, if win condition met, undo simulation and place piece for real
                    if CheckWinner() == tttAI:
                        TttBoard[i] = None
                        placePiece(i)
                        return
                    #undo simulated move if no win
                    TttBoard[i] = None

            #Block player after checking win con (first 3 pieces)
            for i in range(9):
                if TttBoard[i] is None:
                    TttBoard[i] = tttPlayer
                    if CheckWinner() == tttPlayer:
                        TttBoard[i] = None
                        placePiece(i)
                        return
                    TttBoard[i] = None

            # Fallback: using linear search to place new piece
            OPieceFallback()

        elif TttState == TTTState.movement:
            #Try to complete a win by moving a piece
            for from_index in OPieces:
                for to_index in range(9):
                    if TttBoard[to_index] is None:
                        #Simulate the move
                        TttBoard[from_index] = None
                        TttBoard[to_index] = tttAI
                        if CheckWinner() == tttAI:
                            #Win found! Make this move
                            TttBoard[from_index] = None
                            TttBoard[to_index] = None
                            TttSelectedPiece = from_index
                            store.OPiecesPlaced = 2
                            placePiece(to_index)
                            return
                        #Undo simulation
                        TttBoard[from_index] = tttAI
                        TttBoard[to_index] = None

            #Try to block player from winning by using the last index piece
            for from_index in OPieces:
                for to_index in range(9):
                    if TttBoard[to_index] is None:
                        #Simulate the move
                        TttBoard[from_index] = None
                        TttBoard[to_index] = tttPlayer
                        if CheckWinner() == tttPlayer:
                            #Player would win here! Block it
                            TttBoard[from_index] = None
                            TttBoard[to_index] = None
                            TttSelectedPiece = from_index
                            store.OPiecesPlaced = 2
                            placePiece(to_index)
                            return
                        TttBoard[from_index] = tttAI
                        TttBoard[to_index] = None

            # Fallback: using linear search to place old piece
            OPieceFallback()
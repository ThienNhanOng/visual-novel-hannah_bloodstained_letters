init python:
    def aiMove():
        global TttCurrentPlayer, TttState, TttBoard, OPieces, TttSelectedPiece

        if TttState == TTTState.placement:
            #Check if placing will secure win
            for i in range(9):
                if TttBoard[i] is None:
                    TttBoard[i] = tttAI
                    if CheckWinner() == tttAI:
                        TttBoard[i] = None
                        placePiece(i)
                        return
                    TttBoard[i] = None

            #Block player after checking win con
            for i in range(9):
                if TttBoard[i] is None:
                    TttBoard[i] = tttPlayer
                    if CheckWinner() == tttPlayer:
                        TttBoard[i] = None
                        placePiece(i)
                        return
                    TttBoard[i] = None

            #place in any cell if doesn't matter
            for i in range(9):
                if TttBoard[i] is None:
                    placePiece(i)
                    break

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
                            move(to_index)
                            return
                        #Undo simulation
                        TttBoard[from_index] = tttAI
                        TttBoard[to_index] = None

            #Try to block player from winning
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
                            move(to_index)
                            return
                        TttBoard[from_index] = tttAI
                        TttBoard[to_index] = None

            if OPieces:
                from_index = OPieces[0]
                for i in range(9):
                    if TttBoard[i] is None:
                        TttSelectedPiece = from_index
                        move(i)
                        break
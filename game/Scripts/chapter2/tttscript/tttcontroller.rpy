#Player controller

init python:
    #Win condition check
    def CheckWinner():
        for line in tttWin:
            a = line[0]
            b = line[1]
            c = line[2]

            first = TttBoard[a]  
            second = TttBoard[b]
            third = TttBoard[c]

            #Return the last piece played if win was not found
            if first is not None:
                #Check if all x or o is the same
                if first == second and first == third:
                    return first 

        return None

#Switch to ai after play
init python:
    def SwitchPlayer():
        # No need for global TttCurrentPlayer; Ren'Py store handles it

        #change between ai and player
        if TttCurrentPlayer == tttPlayer:
            TttCurrentPlayer = tttAI
            renpy.invoke_in_new_context(aiMove)
        else:
            TttCurrentPlayer = tttPlayer


#Game Mechanic 
init python:
    def placePiece(index):
        
        #Check if cell is empty or not to prevent overwriting
        if TttBoard[index] is not None:
            return

        #check player's piece
        if TttCurrentPlayer == tttPlayer:
            pieces = XPieces
            #check for max 3 pieces
            if XPiecesPlaced == 3:
                return
        else:
        #check ai pieces
            pieces = OPieces
            #check for max 3 pieces
            if OPiecesPlaced == 3:
                return

        #Place the piece onto the board. ui is handled in tttscreen
        TttBoard[index] = TttCurrentPlayer
        pieces.append(index)

        #count for win
        if TttCurrentPlayer == tttPlayer:
            XPiecesPlaced += 1
        else:
            OPiecesPlaced += 1

        afterTurn()

init python:
    def move(index):
        
        #Rule and Boundary check for game board
        #this check if cell is empty to make play
        if TttBoard[index] is not None:
            return

        #Determine which piece x or o to update
        pieces = XPieces if TttCurrentPlayer == tttPlayer else OPieces

        #Use selected piece if set (for AI), otherwise use first piece
        if TttSelectedPiece is not None and TttSelectedPiece in pieces:
            old = TttSelectedPiece
        else:
            old = pieces[0]
            
        TttBoard[old] = None  
        TttBoard[index] = TttCurrentPlayer  

        #after 3 tries remove oldest piece and make it the new last piece
        pieces.remove(old)        
        pieces.append(index) 
        TttSelectedPiece = None
        afterTurn()

init python:
    def afterTurn():
        
        #Reset win flag each turn; will be set true only when player wins
        tttwin = False

        winner = CheckWinner()
        if winner:
            tttwin = (winner == tttPlayer)
            TttState = TTTState.game_over
            renpy.notify(f"the gem opened! ") 
            return

        #Switch to movement phase if both players placed 3 pieces
        if XPiecesPlaced >= 3 and OPiecesPlaced >= 3:
            TttState = TTTState.movement

        #Switch turn
        SwitchPlayer()

#Ai logic moved to tttAI.rpy

#click handler
init python:
    def CellClicked(index):
        if TttState == TTTState.placement:
            placePiece(index)
        elif TttState == TTTState.movement:
            move(index)
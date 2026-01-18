#Player controller

init python:
    #check for winner ai vs player
    def CheckWinner():
        for line in tttWin:
            a = line[0]
            b = line[1]
            c = line[2]

            first = store.TttBoard[a]  
            second = store.TttBoard[b]
            third = store.TttBoard[c]

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
        if store.TttCurrentPlayer == store.tttPlayer:
            store.TttCurrentPlayer = store.tttAI
            renpy.invoke_in_new_context(store.aiMove)
        else:
            store.TttCurrentPlayer = store.tttPlayer


#Game Mechanic 
init python:
    def placePiece(index):
        
        #Check if cell is empty or not to prevent overwriting
        if store.TttBoard[index] is not None:
            return

        #check player's piece
        if store.TttCurrentPlayer == store.tttPlayer:
            pieces = store.XPieces
            #check for max 3 pieces
            if store.XPiecesPlaced == 3:
                return
        else:
            #check ai pieces
            pieces = store.OPieces
            #check for max 3 pieces
            if store.OPiecesPlaced == 3:
                return

        #Place the piece onto the board. ui is handled in tttscreen
        store.TttBoard[index] = store.TttCurrentPlayer
        pieces.append(index)

        #count for win
        if store.TttCurrentPlayer == store.tttPlayer:
            store.XPiecesPlaced += 1
        else:
            store.OPiecesPlaced += 1

        afterTurn()

init python:
    def move(index):
        
        #Rule and Boundary check for game board
        #this check if cell is empty to make play
        if store.TttBoard[index] is not None:
            return

        #Determine which piece x or o to update
        pieces = store.XPieces if store.TttCurrentPlayer == store.tttPlayer else store.OPieces
        old = pieces[0]
            
        store.TttBoard[old] = None  
        store.TttBoard[index] = store.TttCurrentPlayer  

        #after 3 tries remove oldest piece and make it the new last piece
        pieces.remove(old)        
        pieces.append(index) 
        store.TttSelectedPiece = None
        afterTurn()

init python:
    def afterTurn():
        
        #Reset win flag each turn
        store.tttplayerWin = False

        winner = CheckWinner()
        if winner:
            store.tttplayerWin = (winner == store.tttPlayer)
            store.TttState = store.TTTState.game_over
            renpy.notify(f"the gem opened! ") 
            return

        #Switch to movement phase if both players placed 3 pieces
        if store.XPiecesPlaced >= 3 and store.OPiecesPlaced >= 3:
            store.TttState = store.TTTState.movement

        #Switch turn
        SwitchPlayer()

#Ai logic moved to tttAI.rpy

#click handler
init python:
    def CellClicked(index):
        if store.TttState == store.TTTState.placement:
            placePiece(index)
        elif store.TttState == store.TTTState.movement:
            move(index)
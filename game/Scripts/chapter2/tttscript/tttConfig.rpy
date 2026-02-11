init python:
    def resetTTTGame():
        store.TttBoard = [None] * 9
        store.TttCurrentPlayer = store.tttPlayer
        store.TttSelectedPiece = None
        store.XPieces = []
        store.XPiecesPlaced = 0
        store.OPieces = []
        store.OPiecesPlaced = 0
        store.tttplayerWin = False
        store.TttState = store.TTTState.placement
        
#Board: empty slot for pieces
default TttBoard = [None, None, None, None, None, None, None, None, None]
#Track player moves
default TttCurrentPlayer = tttPlayer  #Always X
#selected piece during player turn
default TttSelectedPiece = None

#Track player and ai pieces and placed
default XPieces = []
default XPiecesPlaced = 0
default OPieces = []
default OPiecesPlaced = 0
default tttPlayer = "X"
default tttAI = "O"
default tttAI_first = False

#Track if player won the current session
default tttplayerWin = False

#Current game state
default TttState = TTTState.placement

init python:
    from enum import Enum

    #enum for move placement state 
    class TTTState(Enum):
        placement = 0     #Players place 3 pieces
        movement = 1      #Players move existing pieces
        game_over = 2     #Win when 3 in a row

    #board
    boardSize = 3
    boardCells = boardSize * boardSize

    #board visual
    #0 | 1 | 2
    #3 | 4 | 5
    #6 | 7 | 8

    #Generate win board combinations
    def winBoard():
        #total win combinations
        winCombinations = []

        for row in range(3):
            rowCombination = []  # hold combination for this row
            for col in range(3): #iterate through the columns for the current row
                index = row * 3 + col
                rowCombination.append(index)  #store the combination 
            winCombinations.append(rowCombination)  # add the combination to total combinations
            
        for col in range(3):
            colCombination = []  # hold combination for this column
            for row in range(3):  # iterate through rows for the current column
                index = row * 3 + col  # convert row, col to flat list index
                colCombination.append(index)  # store the combination
            winCombinations.append(colCombination)  # add this column to total combinations

        #2 Diagonals
        winCombinations.append([0, 4, 8])
        winCombinations.append([2, 4, 6])
        
        return winCombinations

    #Generate win combinations based on board size
    tttWin = winBoard()
    #Player marker
    tttPlayer = "X"
    #AI marker
    tttAI = "O"

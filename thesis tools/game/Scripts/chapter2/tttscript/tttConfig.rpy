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

init python:
    # Winning combinations (add this if missing)
    tttWin = (
        (0, 1, 2), #horizontal
        (3, 4, 5), #horizontal
        (6, 7, 8), #horizontal
        (0, 3, 6), #vertical
        (1, 4, 7), #vertical
        (2, 5, 8), #vertical
        (0, 4, 8), #diagonal
        (2, 4, 6), #diagonal
    )

    #Player marker
    tttPlayer = "X"
    #AI marker
    tttAI = "O"

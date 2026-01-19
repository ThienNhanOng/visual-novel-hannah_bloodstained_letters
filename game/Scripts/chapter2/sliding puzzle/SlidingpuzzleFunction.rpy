init python:
    # Use shared shuffle from CreateDeck.rpy
    import renpy.store as store
    #Swap two tiles
    def swap_tiles(index1, index2):
        puzzleState[index1], puzzleState[index2] = puzzleState[index2], puzzleState[index1]

    #Find the blank tile
    def find_blank():
        return puzzleState.index(None)

    #Check if puzzle is solved
    def is_puzzle_solved():
        return puzzleState == puzzleImages

    #Shuffle the puzzle tiles using shared fisherYates
    def shufflePuzzle():
        #make a copy of the original picture before shuffling
        store.puzzleState = store.puzzleImages[:]
        store.puzzle_completed = False
        store.fisherYates(store.puzzleState)

    #Instantly solve puzzle
    def solve_puzzle_instantly():
        store.puzzleState = store.puzzleImages[:]
        store.puzzle_completed = True

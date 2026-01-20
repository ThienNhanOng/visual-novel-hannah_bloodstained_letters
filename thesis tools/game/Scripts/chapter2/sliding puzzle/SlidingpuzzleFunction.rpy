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

    #Check if the current puzzle state is solvable (3x3)
    def is_solvable(puzzleState):
        # Flatten the puzzle, ignore None (blank)
        tiles = [tile for tile in puzzleState if tile is not None]
        inversions = 0
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if puzzleImages.index(tiles[i]) > puzzleImages.index(tiles[j]):
                    inversions += 1
        # Find blank row from bottom (0-based)
        blank_index = puzzleState.index(None)
        blank_row_from_bottom = 2 - (blank_index // 3)
        # For odd grid (3x3), solvable if inversions is even
        return inversions % 2 == 0

    #Shuffle the puzzle tiles using shared fisherYates, repeat until solvable
    def shufflePuzzle():
        #make a copy of the original picture before shuffling
        store.puzzle_completed = False
        while True:
            store.puzzleState = store.puzzleImages[:]
            store.fisherYates(store.puzzleState)
            if is_solvable(store.puzzleState):
                break

    #Instantly solve puzzle
    def solve_puzzle_instantly():
        store.puzzleState = store.puzzleImages[:]
        store.puzzle_completed = True

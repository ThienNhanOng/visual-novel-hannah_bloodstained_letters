init python:
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
        # Assign numbers 1-8 to tiles, None is blank
        tile_numbers = []
        #if tile is None skip it
        for tile in puzzleState:
            if tile is None:
                continue
            #match image with its number 0-8
            try:
                num = int(tile.split('_')[-1].split('.')[0])
            except Exception:
                num = 0
            tile_numbers.append(num)
        #invert list to see if solvable. if it is return
        inversions = 0
        for i in range(len(tile_numbers)):
            for j in range(i + 1, len(tile_numbers)):
                if tile_numbers[i] > tile_numbers[j]:
                    inversions += 1
        # For 3x3 grid, solvable if inversions is even
        return inversions % 2 == 0

    #Shuffle the puzzle tiles using shared fisherYates, repeat inversion until solvable
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

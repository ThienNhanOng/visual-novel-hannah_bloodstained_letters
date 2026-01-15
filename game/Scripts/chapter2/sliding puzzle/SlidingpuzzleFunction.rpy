init python:
    import random
    
    #Swap two tiles
    def swap_tiles(index1, index2):
        puzzleState[index1], puzzleState[index2] = puzzleState[index2], puzzleState[index1]

    #Find the blank tile
    def find_blank():
        return puzzleState.index(None)

    #Check if puzzle is solved
    def is_puzzle_solved():
        return puzzleState == puzzleImages

    #Shuffle puzzle using monte carlo shuffle.
    def shufflePuzzle():
        #make a copy of the original picture before shuffling
        store.puzzleState = store.puzzleImages[:]
        store.puzzle_completed = False
        
        blank = find_blank()
        for i in range(100):
            blank = find_blank()
            neighbors = []
            row = blank // puzzle_cols
            col = blank % puzzle_cols

            #rows are up and down 
            #cols are left and right

            if row > 0: neighbors.append(blank - puzzle_cols)
            if row < puzzle_rows - 1: neighbors.append(blank + puzzle_cols)
            if col > 0: neighbors.append(blank - 1)
            if col < puzzle_cols - 1: neighbors.append(blank + 1)

            swap_tiles(blank, random.choice(neighbors))

    #Instantly solve puzzle
    def solve_puzzle_instantly():
        store.puzzleState = store.puzzleImages[:]
        store.puzzle_completed = True

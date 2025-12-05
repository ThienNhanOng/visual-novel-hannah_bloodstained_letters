init python:
    import random
    
    # Initialize puzzle state
    def init_puzzle():
        global puzzle_state, puzzle_completed
        puzzle_state = puzzle_images[:]  # Copy original image order
        puzzle_completed = False

    # Swap two tiles
    def swap_tiles(index1, index2):
        puzzle_state[index1], puzzle_state[index2] = puzzle_state[index2], puzzle_state[index1]

    # Find the blank tile
    def find_blank():
        return puzzle_state.index(None)

    # Check if puzzle is solved
    def is_puzzle_solved():
        return puzzle_state == puzzle_images

    # Shuffle puzzle
    def shuffle_puzzle():
        init_puzzle()
        blank = find_blank()
        for i in range(100):
            blank = find_blank()
            neighbors = []
            row = blank // puzzle_cols
            col = blank % puzzle_cols

            if row > 0: neighbors.append(blank - puzzle_cols)
            if row < puzzle_rows - 1: neighbors.append(blank + puzzle_cols)
            if col > 0: neighbors.append(blank - 1)
            if col < puzzle_cols - 1: neighbors.append(blank + 1)

            swap_tiles(blank, random.choice(neighbors))

    # Instantly solve puzzle
    def solve_puzzle_instantly():
        global puzzle_state, puzzle_completed
        puzzle_state = puzzle_images[:]
        puzzle_completed = True

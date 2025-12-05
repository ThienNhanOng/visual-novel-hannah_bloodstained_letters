
default puzzle_completed = False
# Screen to show 9-tile sliding puzzle
init python:
    # Function to handle tile clicks
    def click_tile(tile_index):
        global puzzle_completed
        blank_index = find_blank()
        row_tile = tile_index // puzzle_cols
        col_tile = tile_index % puzzle_cols
        row_blank = blank_index // puzzle_cols
        col_blank = blank_index % puzzle_cols

        # Swap if adjacent
        if  (abs(row_tile - row_blank) == 1 and col_tile == col_blank) or \
            (abs(col_tile - col_blank) == 1 and row_tile == row_blank):
            swap_tiles(tile_index, blank_index)
            
            # Check if puzzle is solved after the move
            if is_puzzle_solved():
                puzzle_completed = True

# Puzzle screen
screen sliding_puzzle_screen():
    tag menu

    # Keybinding to instantly solve puzzle
    key "p" action Function(solve_puzzle_instantly)

    frame:
        xalign 0.5
        yalign 0.5
        has grid puzzle_rows puzzle_cols spacing 5

        for i in range(puzzle_rows * puzzle_cols):
            if puzzle_state[i] is not None:
                imagebutton:
                    idle puzzle_state[i]
                    hover puzzle_state[i]
                    focus_mask True
                    action Function(click_tile, i)
            else:
                text " "  # Blank tile placeholder

    if puzzle_completed:
            timer 0.5 repeat False action Return()
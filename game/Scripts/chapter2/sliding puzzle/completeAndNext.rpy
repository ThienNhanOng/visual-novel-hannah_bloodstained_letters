#Scene to verify puzzle is completed
#This prevent screen language bug from occuring

label puzzle_complete_and_next:
    show screen puzzle_complete_screen
    hide screen puzzle_complete_screen
    hide screen sliding_puzzle_screen
    $ renpy.pause(2)
    hide puzzle_complete_image
    scene bg room1
    jump after_puzzle
    

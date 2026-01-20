#Scene to verify puzzle is completed
#This prevent screen language bug from occuring

label puzzle_complete_and_next:
    #Hide game screen to prevent sync issue between screen and language
    show screen puzzle_complete_screen
    hide screen puzzle_complete_screen
    hide screen sliding_puzzle_screen
    $ renpy.pause(2)
    hide puzzle_complete_image
    #Tansitions
    scene bg room1
    jump after_puzzle
    

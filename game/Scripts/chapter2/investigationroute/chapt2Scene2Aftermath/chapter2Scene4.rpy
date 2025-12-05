label Chapter2Scene4_helpingSilas:


    "[Player] Arrived at the school."
    Silas "Thank god you're here. lets hurry to my dorm"
    #shock picture
    $ renpy.pause(1, hard=True)
    Player "What happened? this place is a mess!"
    Silas "I know! they changed my dorm and I havent had time to unpack. please I need help!"
    #picture of messy dorm
    "[Player] helped Silas move his stuff around and unpack."
    centered "After a few hours of hard work Later:"
    # add puzzle mini game

# sliding_puzzle_labels.rpy

    $ shuffle_puzzle()
    "help Silas clean his room"
    window hide
    call screen sliding_puzzle_screen()
    jump after_puzzle



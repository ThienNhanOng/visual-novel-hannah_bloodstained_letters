label investigating_the_school:
    "[Player] Decided to investigate the school."
    #show player 
    #show courtyard picture background
    #show player in courtyard
    #show player walking around the track field
    #show player walking around the school
    "After a day of walking around and wasting time, [Player] found nothing of interest."
    
    Player "Lets recall what that Detective said"
    Player "Ally lurks at school \n hm.."

    #Change player font to yell font
    $ Player = Character("Player", color="#25ffed", what_size=yellFont)
    Player "AHH FUCK THIS."
    #Reset to normal talk font
    $ Player = Character("Player", color="#25ffed", what_size=talkFont)
    "Player plan to return back to town. but first she made a stop at Silas dormitory."
    #todo play knocking sounds
    centered "{b}knock knock{/b}"
    "Silas opened the door."
    Silas "FOR THE LAST TIME, I DONT WANT ANY..."
    Silas "oh..OH! COME IN! Come in!"
    #show player confuse
    Player "so Sy, Im not gonna ask what that was about but anyway,"
    Player "I am about to head back home. Just dropping by to say bye"
    Silas "Oh alright [Player] get home safely!"
    Silas "It was nice seeing you. Thanks again for rescuing me."
   
    if Silas_counter < Theo_counter:
        "As she about to leave to dismiss any rumors, she saw a brochure."
        "It was definitely one that belongs to {i}JT Jewelry{/i}."
        "Is it a coincidence that Sylas is doing an assignment based on the jewelry store? Or is there more to it?"
        "I need to find out more about this."
    else:
        "As she about to leave she saw something that caught her attention. a gem like object."
        Player "what is this Sy?"
        Silas "to be honest no clue. it looks like a gem of some sort. but there is some sort of force"
        Silas "or some sort of energy coming from it. I cant quite explain it."
        Player "it looks like it can be opened"
        Silas "it does doesnt it. i've tried but it wont budge."
        Player "hm.. let me give it a go."
        #if player win continue story otherwise redo scene
        $ tttplayerWin = False
        call screen TicTacToeScreen
        if tttplayerWin:
            "the gem unravel and illuminate itself with red and glitter"
            Player "Hey look! i did it!"
            Silas "really? Lets see..."
            "Inside the gem was a piece of paper."
            "certificate of authenticity. gt auctions."
            "seller of the 'Conan that Ran' a red and precious gem: Hannah"
            "and bidder as well as new owner: mr Edward harper-Chapman"
            "..."
            Player "Chapman? where have i ever heard that name before..."
            "chapman...chapman..."
            Player "chapman...GASP"
            "THEODORE EDWARD HARPER-CHAPMAN..."
            Player "SILAS. I MUST GO IM SORRY."
            "player rushes out after realizing the name."
            "and that the detective may not just be a detective but "
            "the very person behind all of this."

            if storyDecision_Chapter2_InvestigationRoute == False and Silas_counter >= 15:
                jump Chapter2Date
        else:
            #Restart scene if player lose. as well as ttt state
            "You lost."
            $ resetTTTGame()
            jump investigating_the_school
        
    'end of chapter 2'
    $ MainMenu()
    #end of chapter2. 
    #continuation chapter3 will include meeting back up with theo and discussing about her findings.
    #this will ultimately lead to chapter 3 and 4 where more notes will show up leading to the 
    #confrontation with the mystery man. 

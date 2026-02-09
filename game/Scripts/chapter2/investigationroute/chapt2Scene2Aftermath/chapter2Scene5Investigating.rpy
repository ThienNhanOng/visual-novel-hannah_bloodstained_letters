label investigating_the_school:
    "[Player] Decided to investigate the school."
    scene trackbg
    show Player_L1
    #show player 
    #show courtyard picture background
    #show player in courtyard
    #show player walking around the track field
    #show player walking around the school
    "After walking around endlessly and wasting time, [Player] found nothing of interest."
    
    Player "Lets recall what that Detective said"
    Player "Ally lurks at school \n hm.."

    #Change player font to yell font
    $ Player = Character("Player", color="#25ffed", what_size=yellFont)
    Player "AHH FUCK THIS."
    #Reset to normal talk font
    $ Player = Character("Player", color="#25ffed", what_size=talkFont)
    "Player plan to return back to town. but first she made a stop at Silas dormitory."
    #todo play knocking sounds
    centered "{b}{color=#ffffff}{size=172}knock knock{/size}{/color}{/b}"
    "Silas opens the door."
    scene expression im.Scale("slidingpuzzle/organized dormroom.jpg", config.screen_width, config.screen_height)
    show silas talk
    Silas "FOR THE LAST TIME, I DONT WANT ANY..."
    Silas "oh..OH! COME IN! Come in!"
    #show player confuse
    Player "so Sy, Im not gonna ask what that was about but anyway,"
    Player "I am thinking about unenrolling from school."
    Player "it was a good experience. I made some friends, got my first job"
    Player "And I thought i was able to move on as well."
    Player "However... i still think of Hannah from here and there"
    Player "Silas, I think i need to go home. for now at least."
    Silas "say no more. I know youre going through a difficult time."
    Silas "[Player] just get home safely is all I ask!"
   
    

    jump ending
        
    #'end of chapter 2'
    #$ MainMenu()
    #end of chapter2. 
    #continuation chapter3 will include meeting back up with theo and discussing about her findings.
    #this will ultimately lead to chapter 3 and 4 where more notes will show up leading to the 
    #confrontation with the mystery man. 

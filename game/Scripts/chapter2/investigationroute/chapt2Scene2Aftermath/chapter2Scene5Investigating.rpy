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
    # Reset to normal talk font
    $ Player = Character("Player", color="#25ffed", what_size=talkFont)
    "Player plan to return back to town. but first she made a stop at Silas dormitory."
    #todo play knocking sounds
    "{b}{center}knock knock{/center}{/b}"
    "Silas opened the door."
    Silas "FOR THE LAST TIME, I DONT WANT ANY..."
    Silas "oh..OH! COME IN! Come in!"
    #show player confuse
    Player "so Sy, Im not gonna ask what that was about but anyway,"
    Player "I am about to head back home. Just dropping by to say bye"
    Silas "Oh alright [Player] get home safely!"
    Silas "It was nice seeing you. Thanks again for rescuing me."
   
    "As she about to leave to dismiss any rumors, she saw a brochure."
    "It was definitely one that belongs to {i}JT Jewelry{/i}."
    "Is it a coincidence that Sylas is doing an assignment based on the jewelry store? Or is there more to it?"
    "I need to find out more about this."
    
    'test'
return


label after_puzzle: 
    "Phew! all clean and tidy now!"
    #https://www.youtube.com/watch?v=STgjUMPUVn0 idea for puzzle
    #$ puzzle_completed = True  # Set the flag to True
    menu:
        "now that we finish helping Silas, what now?"

        "Investigate":
            Player "Lets recall what that Detective said"
            Player "Ally lurks at school \n hm.."
            jump investigating_the_school #short ending
            
        "prepare to go home for the day:": #give up route and enroll player into school
            
            centered "player returned home"
            jump testlabel
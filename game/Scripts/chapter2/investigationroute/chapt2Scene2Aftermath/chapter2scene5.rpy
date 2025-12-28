label after_puzzle: 
    "Phew! all clean and tidy now!"
    #https://www.youtube.com/watch?v=STgjUMPUVn0 idea for puzzle
    #$ puzzle_completed = True  # Set the flag to True
    "now that we finish helping Silas, what now?"

    menu:
        "Investigate" if Theo_counter >= 5 or Silas_counter >= 4:
            Player "Lets recall what that Detective said"
            Player "Ally lurks at school \n hm.."
            jump investigating_the_school #short ending

        "Prepare to go home for the day": # give up route and enroll player into school
            # this route will happen if player does not have enough theo counter or if selected by choice.
            centered "player returned home"

    jump testlabel
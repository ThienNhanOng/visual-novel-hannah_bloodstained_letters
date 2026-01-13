label afterpuzzle: 
    "Phew! all clean and tidy now!"
    #https://www.youtube.com/watch?v=STgjUMPUVn0 idea for puzzle
    #$ puzzlecompleted = True  #Set the flag to True
    "now that we finish helping Silas, what now?"
    
    #hidden menu requires theo counter or silas counter to be high enough.
    menu:
        "Investigate" if Theocounter >= 5 or Silascounter >= 4:
            Player "Lets recall what that Detective said"
            Player "Ally lurks at school \n hm.."
            jump investigatingtheschool #short ending

        "Prepare to go home for the day": #give up route and enroll player into school
            #this route will happen if player does not have enough theo counter or if selected by choice.
            centered "player returned home"
            Player "day after day and still no leads..."
            "on my way home, I ran into Mia."
            Mia "Hey [Player], what are you doing here?"
            Mia "need a ride?"
            Player "oh hey Mia, yeah...I'd like that."
            $ chapter2continue = True
            call chapter1scene3Peaceful #reuse scene where player takes a ride.

    jump testlabel
#placeholder test
label gameroom:
    
    scene blackscreen 
    stop music fadeout 2.0
    
    if (arcadeUnlocked == True):
        menu:
            "Yes, I want to play (cost $10)":
                if Global_Money >= 10:
                    $ Global_Money -= 10
                    $ jump_score = 0  #Reset score for new game
                    $ game = None  #Will be initialized below

                    #Initialize game safely
                    $ game = SimpleGameState()

                    play music "Scripts/chapter2/jumping_game/ninja racer stuff/Pixel Highway.wav" fadein 10.0 loop

                    call screen jump_game
                    stop music fadeout 2.0
                    #reward player money 
                    $ Global_Money += int(round(jump_score / 100.0) * 10)  #Convert 100 points = 10 dollars
                    jump lostscreen
                else:
                    "You need at least $10 to play."
            "No, thanks":
                "What a shame. Maybe next time."
    else:
        "You checked out the gameroom but it seems to be locked."
    #increase time after leaving the room
    $ timeIncrease()
    stop music fadeout 2.0
    jump schoolmap
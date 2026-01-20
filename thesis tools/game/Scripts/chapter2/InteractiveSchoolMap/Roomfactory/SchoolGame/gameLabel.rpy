#placeholder test
default enemy_manager = None
default projectileManager = None
label gameroom:
    
    #scene blackscreen 
    stop music fadeout 2.0
    
    if (arcadeUnlocked == True):
        menu:
            "Play ninja jumper(cost $10)":
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
            "play cubic shooter(cost $20) no rewards":
                if Global_Money >= 20:
                    
                    $ Global_Money -= 20                  
                    call instructions_shootinggame
                    notify "You earned no money from this game."
                else:
                    "You need at least $20 to play."
            "no thank you":
                "Thats a shame maybe next time."
    else:
        "You checked out the gameroom but it seems to be locked."
    #increase time after leaving the room
    $ timeIncrease()
    stop music fadeout 2.0
    jump schoolmap
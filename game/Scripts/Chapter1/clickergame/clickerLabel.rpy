#Wrapper label: call this to run the mini-game and get the final score back.
label clickergame:
    $ game = ClickerGame.get_instance()
    $ game.score = 0
    $ game.misclicks = 0
    $ game.sizePixels = 140
    $ game.relocateaxe = 1.8
    
    call screen clicker_minigame
    
    #Check score and update counters
    if game.score >= 5 and game.score <= 10:
        $ Mia_counter += 1
    elif game.score >= 10:
        $ Theo_counter += 1
    
    "Reward-counter: mia | [Mia_counter] | silas [Silas_counter] | theo [Theo_counter]|"
    return

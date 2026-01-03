screen clicker_minigame():
    modal True
    $ game = ClickerGame.get_instance()

    #lose condition
    if game.is_game_over():
        add "images/chapter2/forestroompictures/need remove bg/axe.jpeg"

        frame:
            xalign 0.5
            yalign 0.4
            padding (20, 20)
            has vbox
            text "Game Over" size 60 xalign 0.5
            text "Score: [game.score]" size 40 xalign 0.5

        timer 0.1 action Return(game.score)

    #gameplay screen
    else:
        

        # hud: Score, Misses, State
        frame:
            xalign 0.02
            yalign 0.02
            padding (12, 8)

            #vbox container for hud elements
            has vbox
            hbox:
                text "Score: [game.score]" size 26
                text "Miss clicked: [game.misclicks]/3" size 26
            text "State: [game.state.name()]" size 18 color "#888888"

        # timers for game updates
        timer game.relocate_interval repeat True action Function(game.respawn_target)
        #relocate axe
        timer 0.05 repeat True action Function(game.update_animation)
        timer 0.05 repeat True action Function(game.update_state)

        # background clickable area
        button:
            xfill True
            yfill True
            background None
            action Function(game.click_background)

        #axe hitbox
        button:
            align (game.target_x, game.target_y)
            xsize game.size_pixels
            ysize game.size_pixels
            background None
            hover_background None

            # display target sprite if available
            if renpy.loadable("images/axenobg.png"):
                add im.Scale("images/axenobg.png", game.size_pixels, game.size_pixels)
            else:
                # transparent fallback hitbox
                add Solid("#0000")

            action Function(game.click_target)


label clickergame:
    
    $ game = ClickerGame.get_instance()
    $ game.__init__()  # reset the game
    call screen clicker_minigame
    
    # apply rewards based on score
    if _return >= 5 and _return <= 10:
        $ Mia_counter += 1
    elif _return >= 10:
        $ Theo_counter += 1
    
    "Reward-counter: mia | [Mia_counter] | silas [Silas_counter] | theo [Theo_counter]|"
    
    return _return


init:
    #Images setup
    # Paths include the Scripts folder so Ren'Py loads the assets from
    # the Scripts subdirectory where they currently live.
    image player_stand = "Scripts/chapter2/jumping_game/ninja racer stuff/standstate.png"
    # jump is scaled.
    image player_jump = Transform("Scripts/chapter2/jumping_game/ninja racer stuff/jumpstate.png", xzoom=3.0, yzoom=3.0)
    # background
    image background = "Scripts/chapter2/jumping_game/ninja racer stuff/background.jpeg"

    image car = "Scripts/chapter2/jumping_game/ninja racer stuff/racecar.png"

    image blackscreen:
        "Scripts/chapter2/jumping_game/ninja racer stuff/blackscreen.png"
        size (config.screen_width, config.screen_height)

    image lostscreenimage:
        "Scripts/chapter2/jumping_game/ninja racer stuff/endscreen.jpeg"
        size (config.screen_width, config.screen_height)
    
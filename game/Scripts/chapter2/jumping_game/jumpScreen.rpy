screen jump_game():
    tag jump_game
    
    # Capture input so left-clicks do not pass through to the main script
    # (prevents accidental advancing / ending the game).
    modal True

    #renpy binding for space.
    key "K_SPACE" action Function(jumpGame_space)

    # Background
    add Solid("#202020") xysize (8000, game.Screen_Height)

    # Floor
    add Solid("#555555") xysize (8000, 8) ypos game.Floor_Y

    # pixel background (use correct path under Scripts)
    add "Scripts/chapter2/jumping_game/ninja racer stuff/background.jpeg" xalign 0.55 yalign -0.15 xzoom 1.8

    # invoke jump state animation for standing and jumping
    add ("player_stand" if game.player.grounded else "player_jump") xysize (game.player.PlayerWidth, game.player.PlayerHeight) xpos int(game.player.Player_X) ypos int(game.player.Player_Y)

    # Enemy car
    #add Solid("#cc0000") xysize (game.enemy.width, game.enemy.height) xpos int(game.enemy.pos.x) ypos int(game.enemy.pos.y)
    add ("car") xysize (game.enemy.EnemyWidth+45, game.enemy.EnemyHeight+2) xpos int(game.enemy.Enemy_X) ypos int(game.enemy.Enemy_Y + 10)
    # Update the game every frame
    timer 0.016 repeat True action Function(lambda: game.update())

    #add Solid("#000") xysize (config.screen_width, config.screen_height) zorder -5
    #HUD instructions and score    
    text "Press SPACE to jump!" size 80 xpos 668 ypos 820 color "#ffffff"
    text "Score: [jump_score]" size 45 xpos 50 ypos 730 color "#ffffff"

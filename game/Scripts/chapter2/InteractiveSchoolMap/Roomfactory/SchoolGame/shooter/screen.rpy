default shooterScore = 0
default shooterProjectileManager = None
default shooterEnemyManager = None
default shooterEnemySpeedCounter = 0



init:
    image characterRed = Solid("#ff0000", xsize=50, ysize=50)
    image bullet = Solid("#ffff00", xsize=10, ysize=10)
    image enemy = Solid("#00e900", xsize=50, ysize=50)
    image boarderline = Solid("#6d3705", xsize=20, ysize=1080)


    
screen ShooterGameScreen:
    #lock input to the screen
    modal True
    
    # Auto-return when health depleted
    if shooterHealth <= 0:
        timer 0.01 action Return()

    #debug/text label
    #text "X: [shooterSquareX] Y: [shooterSquareY]" xpos 10 ypos 10
    text "Health" xpos 10 ypos 50
    text "[shooterHealth]" xpos 10 ypos 70
    text "Points" xpos 10 ypos 100
    text "[shooterScore]" xpos 10 ypos 120

    #player
    timer 0.01 action updateSquare repeat True
    add "characterRed" xpos (shooterSquareX - 25) ypos (shooterSquareY - 25)

    #bullets
    timer 0.01 action updateProjectiles repeat True
    for bullet in store.shooterProjectileManager.shooterBullets:
        add "bullet" xpos (bullet[0] - 5) ypos (bullet[1] - 5)

    #enemies
    timer 0.01 action updateEnemy repeat True
    add "enemy" xpos (store.shooterEnemyManager.shooterEnemyX - 25) ypos (store.shooterEnemyManager.shooterEnemyY - 25)

    #map
    add "boarderline" xpos 250 ypos 0

    if shooterHealth <= 0:
        # Game over state - show return button
        text "Game Over!" xalign 0.5 yalign 0.5 size 60
        textbutton "Return" action Return() xalign 0.5 yalign 0.6
image cubeshooterbackground = "images/cubeshooterbackground.png"

label instructions_shootinggame:
    scene black
    show cubeshooterbackground:
        xpos 250
        xsize 2080
        ysize 1920
    centered "{color=#ffffff}{b}Shooting Game Instructions{/b}{/color}"
    centered "{color=#ffffff}{b}Use the arrow keys to move your character.
    \nPress the spacebar to shoot" 
    play music "Scripts/chapter2/jumping_game/ninja racer stuff/Pixel Highway.wav" fadein 10.0 loop
    # Initialize managers
    $ shooterProjectileManager = ShooterProjectileManager()
    $ shooterEnemyManager = ShooterEnemyManager()
    call screen ShooterGameScreen
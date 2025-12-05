init python:

    #Debug issue for renpy not detecting update for score.
    #Uses renpy api instead of direct storing access
    from renpy import exports as renpy
    import renpy.store as store


    class SimpleGameState:
        Screen_Width = 1280
        Screen_Height = 720
        Floor_Y = Screen_Height - 120

        #constructor.
        #Initialize player and enemy
        def __init__(self):
            self.player = JumpPlayer(120, self.Floor_Y - 60)
            self.enemy = Enemy(self.Screen_Width, self.Floor_Y - 60)
            self.ended = False


        #Time manager cant work outside renpy.
        #Time manager breaks when trying to run in renpy.



        def update(self):
            if self.ended:
                return

            player = self.player
            enemy = self.enemy

            # Gravity.
            player.Playervelocity_Y += 2
            player.Player_Y += player.Playervelocity_Y

            # Floor collision for player
            if player.Player_Y + player.PlayerHeight >= self.Floor_Y:
                player.Player_Y = self.Floor_Y - player.PlayerHeight
                player.Playervelocity_Y = 0
                player.grounded = True
            else:
                player.grounded = False

            # Call update for Enemy movement
            # This makes sure the enemy updates/moves within the window width.
            enemy.update(self.Screen_Width)

            # Scoring
            # Check for enemy passed player
            if not getattr(enemy, 'passed', False) and (enemy.Enemy_X + enemy.EnemyWidth) < player.Player_X:
                enemy.passed = True

                # keeping the score using renpy.store 
                store.jump_score = getattr(store, 'jump_score', 0) + 10

                # Increase enemy speed by 1 each time player jump over
                if hasattr(enemy, 'Enemy_velocity_X'):
                    enemy.Enemy_velocity_X += -1 if enemy.Enemy_velocity_X < 0 else 1
                if hasattr(enemy, 'vx'):
                    enemy.vx = enemy.velocity_x

            #Collision check for player and enemy
            if (
                player.Player_X < enemy.Enemy_X + enemy.EnemyWidth and
                player.Player_X + player.PlayerWidth > enemy.Enemy_X and
                player.Player_Y < enemy.Enemy_Y + enemy.EnemyHeight and
                player.Player_Y + player.PlayerHeight > enemy.Enemy_Y
            ):
                self.ended = True
                renpy.hide_screen("jump_game")
                renpy.notify("Game Over! You hit the enemy.")
                renpy.notify(f"You scored: {store.jump_score}")
                renpy.music.stop("Scripts/chapter2/jumping_game/ninja racer stuff/Pixel Highway.wav")
                
                #renpy.end_interaction() #end game then return
                return "game over"
#todo convert score to money later.


    # Jump action - math stuff gravity bla bla it makes the jump at 32.
    def jumpGame_space():
        if not game.ended:
            game.player.jump(32)
            #play sound
            renpy.play("Scripts/chapter2/jumping_game/ninja racer stuff/jump noise.wav")

# Lazy singleton. use with renpy existing creation since there can only
# be one game state at a time.
#TODO: replace with actual implemented singleton later


default jump_score = 0
default game = SimpleGameState()

#reset game using hard python by reinitializing game state.
init python:
    def reset_Jumpgame():
        global game
        import renpy.store as store
        from renpy import exports as renpy

        #reward before resetting score
        #I decided to put that in gameroom.rpy instead
        
        #reset score 
        store.jump_score = 0
        game = SimpleGameState()
        renpy.restart_interaction()
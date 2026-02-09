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

        def update(self):
            if self.ended:
                return

            player = self.player
            enemy = self.enemy

            #velocity is the speed of the jump when going up
            player.PlayervelocityY += 2
            player.PlayerY += player.PlayervelocityY

            #Floor collision for player
            if player.PlayerY + player.PlayerHeight >= self.Floor_Y:
                player.PlayerY = self.Floor_Y - player.PlayerHeight
                player.PlayervelocityY = 0
                player.grounded = True
            else:
                player.grounded = False

            #Call update for Enemy movement
            #This makes sure the enemy updates/moves within the window width.
            enemy.update(self.Screen_Width)

            #Scoring
            #getter for enemy
            if not getattr(enemy, 'passed', False) and (enemy.EnemyX + enemy.EnemyWidth) < player.PlayerX:
                enemy.passed = True

                #keeping the score using renpy.store 
                store.jump_score = getattr(store, 'jump_score', 0) + 10

                #setter for enemy speed by 1 each time player jump over
                if hasattr(enemy, 'EnemyvelocityX'):
                    enemy.EnemyvelocityX += -1 if enemy.EnemyvelocityX < 0 else 1
                if hasattr(enemy, 'vx'):
                    enemy.vx = enemy.velocity_x

            #Collision check for player and enemy
            if (
                player.PlayerX < enemy.EnemyX + enemy.EnemyWidth and
                player.PlayerX + player.PlayerWidth > enemy.EnemyX and
                player.PlayerY < enemy.EnemyY + enemy.EnemyHeight and
                player.PlayerY + player.PlayerHeight > enemy.EnemyY
            ):
                self.ended = True
                renpy.hide_screen("jump_game")
                renpy.notify("Game Over! You hit the enemy.")
                renpy.notify(f"You scored: {store.jump_score}")
                renpy.music.stop("Scripts/chapter2/InteractiveSchoolMap/Roomfactory/schoolGame/jumpingGame/ninja racer stuff/Pixel Highway.wav")
                
                #renpy.end_interaction() #end game then return
                return "game over"
            
    #Jump action - math stuff gravity bla bla it makes the jump go up to 32.
    def jumpGame_space():
        if not game.ended:
            game.player.jump(32)
            #play sound
            renpy.play("Scripts/chapter2/InteractiveSchoolMap/Roomfactory/schoolGame/jumpingGame/ninja racer stuff/jump noise.wav")

default jump_score = 0
default game = SimpleGameState()

#reset game using hard python by reinitializing game state.
init python:
    def reset_Jumpgame():

        #give python access to renpy api functions.
        import renpy.store as store
        from renpy import exports as renpy

        #reward before resetting score
        #I decided to put that in gameroom.rpy instead
        
        #reset score 
        store.jump_score = 0
        store.game = SimpleGameState()
        renpy.restart_interaction()
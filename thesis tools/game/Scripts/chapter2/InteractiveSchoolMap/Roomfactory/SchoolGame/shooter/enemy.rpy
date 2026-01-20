init python:
    import pygame
    import random
    #note: __ = do not touch.
    class ShooterEnemyManager:
        def __init__(self):
            #define the position, speed, hitbox, for the enemy object itself
            self.shooterEnemyX = 1800
            self.shooterEnemyY = random.randint(100, 1000)
            self.shooterSpeed = random.randint(5, 20)
            # Create and update enemy hitbox
            self.shooterEnemyRect = pygame.Rect(0, 0, 50, 50)

        #delete enemy
        def __getstate__(self):
            state = self.__dict__.copy()
            if 'shooterEnemyRect' in state:
                del state['shooterEnemyRect']
            return state

        #restore enemy 
        def __setstate__(self, state):
            self.__dict__.update(state)
            self.shooterEnemyRect = pygame.Rect(0, 0, 50, 50)
            self.update_shooter_rect()

        #spawn the restored enemy
        def spawnEnemy(self):
            self.shooterEnemyX = 1800
            self.shooterEnemyY = random.randint(100, 1000)
            self.shooterSpeed = random.randint(5, 20)
            self.update_shooter_rect()

        def update_shooter_rect(self):
            self.shooterEnemyRect.topleft = (self.shooterEnemyX - 25, self.shooterEnemyY - 25)

        #update the enemy to move Left * speed
        def update(self):
            self.shooterEnemyX -= self.shooterSpeed

            # Update enemy's hitbox position
            self.update_shooter_rect()

            # If enemy reaches the left side, damage player and reset enemy
            if self.shooterEnemyX < 250:
                store.shooterHealth -= 10
                self.shooterSpeed = 1
                #bounce back effect
                self.shooterEnemyX = 400
                store.shooterEnemySpeedCounter += 1
                self.update_shooter_rect()   # reposition rect after reset

            #pygame collision detection using rects
            shooterBullets = store.shooterProjectileManager.shooterBullets

            for bullet in shooterBullets[:]:
                #Bullet area
                bullet_rect = pygame.Rect(
                    bullet[0] - 5,      # left
                    bullet[1] - 5,      # top
                    10, 10              # width, height
                )
                #if bullet area collides with enemy area
                if self.shooterEnemyRect.colliderect(bullet_rect):
                    shooterBullets.remove(bullet)
                    self.spawnEnemy()
                    store.shooterScore += 10
                    break   #

            # Restart Renpy to update the screen
            renpy.restart_interaction()

    #instance of enemy manager
    shooterEnemyManager = ShooterEnemyManager()
    store.shooterEnemyManager = shooterEnemyManager

    #Call this to update the enemy each frame
    def updateEnemy():
        shooterEnemyManager.update()

    
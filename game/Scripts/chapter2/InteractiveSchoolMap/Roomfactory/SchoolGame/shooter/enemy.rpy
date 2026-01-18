init python:
    import pygame
    import random

    class ShooterEnemyManager:
        def __init__(self):
            self.shooterEnemyX = 1800
            self.shooterEnemyY = random.randint(100, 1000)
            self.shooterSpeed = random.randint(5, 20)
            #create and update enemy hitbox
            self.shooterEnemyRect = pygame.Rect(0, 0, 50, 50)   # matches image size

        def __getstate__(self):
            state = self.__dict__.copy()
            if 'shooterEnemyRect' in state:
                del state['shooterEnemyRect']
            return state

        def __setstate__(self, state):
            self.__dict__.update(state)
            self.shooterEnemyRect = pygame.Rect(0, 0, 50, 50)
            self.update_shooter_rect()

        def spawnEnemy(self):
            self.shooterEnemyX = 1800
            self.shooterEnemyY = random.randint(100, 1000)
            self.shooterSpeed = random.randint(5, 20)
            self.update_shooter_rect()

        def update_shooter_rect(self):
            self.shooterEnemyRect.topleft = (self.shooterEnemyX - 25, self.shooterEnemyY - 25)

        def update(self):
            # Move enemy
            self.shooterEnemyX -= self.shooterSpeed

            # Update enemy's rect position every frame
            self.update_shooter_rect()

            # Enemy reached left side → damage player
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

            renpy.restart_interaction()

    #instance of enemy manager
    shooterEnemyManager = ShooterEnemyManager()
    store.shooterEnemyManager = shooterEnemyManager

    def updateEnemy():
        shooterEnemyManager.update()

    
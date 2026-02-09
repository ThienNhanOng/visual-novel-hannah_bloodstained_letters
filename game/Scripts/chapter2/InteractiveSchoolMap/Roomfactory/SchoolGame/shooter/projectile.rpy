init python:
    import pygame 
    class ShooterProjectileManager:
        def __init__(self):
            self.shooterBullets = [] #store position of multiple bullets
            self.shooterSpaceClick = False #track the last space click
            self.shooterProjectileSpeed = 10  # Speed of projectiles moving right
        
        #key manager
        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not self.shooterSpaceClick:
                self.shooterBullets.append((shooterSquareX, shooterSquareY))
            
            self.shooterSpaceClick = keys[pygame.K_SPACE]
            
            #track the numbers of shot bullets and move them right
            for i in range(len(self.shooterBullets)):
                bulletX, bulletY = self.shooterBullets[i]
                self.shooterBullets[i] = (bulletX + self.shooterProjectileSpeed, bulletY)
            
            # Remove bullets if reach a specific distance.
            for bullet in self.shooterBullets[:]:
                if bullet[0] >= 1700:
                    self.shooterBullets.remove(bullet)

    shooterProjectileManager = ShooterProjectileManager()
    store.shooterProjectileManager = shooterProjectileManager

    def updateProjectiles():
        shooterProjectileManager.update()
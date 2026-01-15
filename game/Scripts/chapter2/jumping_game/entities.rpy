init python:
    import random

    #Player class
    class JumpPlayer:
        def __init__(self, x, y, w=40, h=60):
            #position
            self.PlayerX = x
            self.PlayerY = y

            #velocity
            self.PlayervelocityX = 0
            self.PlayervelocityY = 0

            #Player size
            self.PlayerWidth = w
            self.PlayerHeight = h

            #check player grounded after jump
            self.grounded = True

        #jump method for player
        def jump(self, power=32):
            if self.grounded: #Only allow jump if grounded
                self.PlayervelocityY = -power
                self.grounded = False


    #Enemy class
    class Enemy:
        def __init__(self, x, y, speed=-4, w=40, h=60):
            #position
            self.EnemyX = x
            self.EnemyY = y
            #enemy size
            self.EnemyWidth = w
            self.EnemyHeight = h
            #speed moving left
            self.EnemyvelocityX = speed

            #has player passed this enemy? flag for scoring
            self.passed = False

        #move enemy
        def update(self, screen_width):
            self.EnemyX += self.EnemyvelocityX #Make the enemy move left

            #If enemy goes off screen, respawn on the right
            if self.EnemyX + self.EnemyWidth < 0:
                #Set random spawn location of enemy 
                offset = random.randint(-200, 500)
                self.EnemyX = screen_width + offset #set the pixel position for spawning
                self.passed = False

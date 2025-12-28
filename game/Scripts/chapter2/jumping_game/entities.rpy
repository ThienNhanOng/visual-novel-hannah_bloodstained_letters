init python:
    import random

    # Player class
    class JumpPlayer:
        def __init__(self, x, y, w=40, h=60):
            # position
            self.Player_X = x
            self.Player_Y = y

            # velocity
            self.Playervelocity_X = 0
            self.Playervelocity_Y = 0

            #Player size
            self.PlayerWidth = w
            self.PlayerHeight = h

            #check player grounded after jump
            self.grounded = True

        # jump method for player
        def jump(self, power=32):
            if self.grounded:
                self.Playervelocity_Y = -power
                self.grounded = False


    # Enemy class
    class Enemy:
        def __init__(self, x, y, speed=-4, w=40, h=60):
            # position
            self.Enemy_X = x
            self.Enemy_Y = y
            #enemy size
            self.EnemyWidth = w
            self.EnemyHeight = h
            # speed moving left
            self.Enemy_velocity_X = speed

            # has player passed this enemy? for scoring
            self.passed = False

        # move enemy
        def update(self, screen_width):
            self.Enemy_X += self.Enemy_velocity_X

            # if enemy goes off screen, respawn on the right
            if self.Enemy_X + self.EnemyWidth < 0:
                offset = random.randint(-200, 500)
                self.Enemy_X = screen_width + offset
                self.passed = False

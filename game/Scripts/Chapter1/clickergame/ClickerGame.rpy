init python:
    import random, math

    class ClickerGame:

        #constructor to setup initial variables
        def __init__(self):
            #axe current position and size when drawn
            self.targetX = 0.5
            self.targetY = 0.5
            self.sizePixels = 140

            #start axe position before sliding
            #past screen boundaries.
            self.startX = 0.5
            self.startY = 0.5
            self.destX = 0.5
            self.destY = 0.5
            self.progress = 0.0 #track progression during slide. 1.0 = done
            self.isSliding = False
            self.slideDuration = 1.0 #time to finish

            #score and misses variables
            self.score = 0
            self.misclicks = 0
            self.relocateaxe = 1.8

            self.state = IdleState(self)

        #update the current state when called by screen timer
        def update_state(self):
            """update current state each frame."""
            self.state.update()

        #input handlers
        def clickTarget(self):
            self.state.clickTarget()

        def click_background(self):
            self.state.click_background()

        def hit_target(self):
            """player hits the target."""
            self.score += 1
            renpy.sound.play("audio/MusicAndSoundtracks/bell.wav", channel="sound")

            #make target slightly smaller and faster
            self.sizePixels = max(120, int(self.sizePixels * 0.95))
            self.relocateaxe = max(0.5, self.relocateaxe * 0.99)

            #move target to a new location
            self.respawnTarget()

        def miss_click(self):
            """player clicks background."""
            self.misclicks += 1

        def respawnTarget(self):
            """pick a new random target location and reset animation."""
            sw, sh = config.screen_width, config.screen_height

            #keep axe in height and width in screen boarder
            marginX = max(0, self.sizePixels / sw * 0.5)
            marginY = max(0, self.sizePixels / sh * 0.5)

            #set animation start and destination
            self.startX, self.startY = self.targetX, self.targetY
            self.destX = random.uniform(marginX, 1 - marginX)
            self.destY = random.uniform(marginY, 1 - marginY)

            self.progress = 0.0
            self.isSliding = True

            #slide duration based on distance (short hops faster)
            dx = self.destX - self.startX
            dy = self.destY - self.startY
            distance = math.hypot(dx, dy)
            #to adjust speed based on distance needed to cover
            self.slideDuration = max(0.35, min(1.2, distance * 1.8))

        def update_animation(self):
            """update target position for smooth sliding."""
            if not self.isSliding:
                return
            
            
            #increment the number of step to progress the animation frames.
            step = 0.05 / self.slideDuration
            self.progress = min(1.0, self.progress + step)

            #Increase smoothness
            #Slide base on time
            t = self.progress
            #smooth formula t^2(3-2t) maps linear t to smooth curve
            tSmooth = t * t * (3 - 2 * t)

            #update target position
            self.targetX = self.startX + (self.destX - self.startX) * tSmooth
            self.targetY = self.startY + (self.destY - self.startY) * tSmooth

            #end of animation
            if self.progress >= 1.0:
                self.isSliding = False
                self.targetX = self.destX
                self.targetY = self.destY

        def is_game_over(self):
            """check if player has missed 3 times."""
            return self.misclicks >= 3


default clicker_game = ClickerGame()

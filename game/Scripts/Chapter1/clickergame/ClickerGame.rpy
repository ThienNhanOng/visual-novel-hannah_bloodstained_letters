init python:
    import random, math

    class ClickerGame:
        _instance = None  # singleton

        def __init__(self):
            #axe target position and size
            self.target_x = 0.5
            self.target_y = 0.5
            self.size_pixels = 140

            #axe animation state
            self.start_x = 0.5
            self.start_y = 0.5
            self.dest_x = 0.5
            self.dest_y = 0.5
            self.progress = 0.0
            self.is_sliding = False
            self.slide_duration = 1.0

            #score and misses variables
            self.score = 0
            self.misclicks = 0
            self.relocate_interval = 1.8

            self.state = IdleState(self)

        #singleton
        @classmethod
        def get_instance(cls):
            if cls._instance is None:
                cls._instance = cls()
            return cls._instance

        #state change
        def change_state(self, new_state):
            """switch to a new state and call enter/exit hooks."""
            self.state.on_exit(self)
            self.state = new_state
            self.state.on_enter(self)

        def update_state(self):
            """update current state each frame."""
            self.state.update()

        #input handlers
        def click_target(self):
            self.state.click_target()

        def click_background(self):
            self.state.click_background()



        def hit_target(self):
            """player hits the target."""
            self.score += 1
            renpy.sound.play("audio/MusicAndSoundtracks/bell.wav", channel="sound")

            # make target slightly smaller and faster
            self.size_pixels = max(120, int(self.size_pixels * 0.95))
            self.relocate_interval = max(0.5, self.relocate_interval * 0.99)

            # move target to a new location
            self.respawn_target()

        def miss_click(self):
            """player clicks background."""
            self.misclicks += 1

        # ------------------------
        # target movement
        # ------------------------
        def respawn_target(self):
            """pick a new random target location and reset animation."""
            sw, sh = config.screen_width, config.screen_height

            # keep target fully visible on screen
            margin_x = max(0, self.size_pixels / sw * 0.5)
            margin_y = max(0, self.size_pixels / sh * 0.5)

            # set animation start and destination
            self.start_x, self.start_y = self.target_x, self.target_y
            self.dest_x = random.uniform(margin_x, 1 - margin_x)
            self.dest_y = random.uniform(margin_y, 1 - margin_y)

            self.progress = 0.0
            self.is_sliding = True

            # slide duration based on distance (short hops faster)
            dx = self.dest_x - self.start_x
            dy = self.dest_y - self.start_y
            distance = math.hypot(dx, dy)
            self.slide_duration = max(0.35, min(1.2, distance * 1.8))

        def update_animation(self):
            """update target position for smooth sliding."""
            if not self.is_sliding:
                return

            # increment progress based on slide duration
            step = 0.05 / self.slide_duration
            self.progress = min(1.0, self.progress + step)

            # smooth interpolation (ease-in-out)
            t = self.progress
            t_smooth = t * t * (3 - 2 * t)

            # update target position
            self.target_x = self.start_x + (self.dest_x - self.start_x) * t_smooth
            self.target_y = self.start_y + (self.dest_y - self.start_y) * t_smooth

            # end of animation
            if self.progress >= 1.0:
                self.is_sliding = False
                self.target_x = self.dest_x
                self.target_y = self.dest_y

        def is_game_over(self):
            """check if player has missed 3 times."""
            return self.misclicks >= 3

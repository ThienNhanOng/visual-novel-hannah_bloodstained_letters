init python:
    import renpy

    
    class ClickerState:
       

        #on click axe
        def click_target(self):
            return

        #click the background
        def click_background(self):
            return  # do nothing by default

        #frame update
        def update(self):
            return  # do nothing by default

        def name(self):
            return self.__class__.__name__


    #idle state
    class IdleState(ClickerState):
        def __init__(self, game):
            self.game = game  # store a reference to the game

        def click_target(self):
            # First click hits the target
            self.game.hit_target()
            # Change state to ClickingState (player is now actively clicking)
            self.game.state = ClickingState(self.game)

        #click background
        def click_background(self):
            self.game.miss_click()
            self.game.state = MissState(self.game)

    class ClickingState(ClickerState):
        def __init__(self, game):
            self.game = game
            # Track when the player last clicked the target
            self.last_click_time = renpy.get_game_runtime()

        def click_target(self):
            #reset last click timer
            self.last_click_time = renpy.get_game_runtime()
            self.game.hit_target()

        def click_background(self):
            # player missed while clicking
            self.game.miss_click()
            self.game.state = MissState(self.game)

        def update(self):
            # if player stops clicking for more than 2 seconds, go back to Idle
            if renpy.get_game_runtime() - self.last_click_time > 2.0:
                self.game.state = IdleState(self.game)


    #penalty after missing state
    class MissState(ClickerState):
        def __init__(self, game):
            self.game = game
            self.start_time = renpy.get_game_runtime()  # time when penalty started
            self.duration = 0.3  # penalty duration in seconds

        def update(self):
            # after penalty duration, return to Idle state
            if renpy.get_game_runtime() - self.start_time > self.duration:
                self.game.state = IdleState(self.game)

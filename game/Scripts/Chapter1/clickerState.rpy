init python:
    import renpy

    # --- Base input state ---
    class ClickerState:
        def on_enter(self, game): pass
        def on_exit(self, game): pass
        def handle_target_click(self, game): pass
        def handle_background_click(self, game): pass
        def update(self, game): pass
        def name(self):
            return self.__class__.__name__

    # --- Idle state: waiting for first click ---
    class IdleState(ClickerState):
        def handle_target_click(self, game):
            game.hit_target()
            game.set_state(ClickingState())

        def handle_background_click(self, game):
            game.miss_click()
            game.set_state(MissState())

    # --- Clicking state: actively clicking target ---
    class ClickingState(ClickerState):
        def __init__(self):
            self.last_click_time = 0

        def on_enter(self, game):
            self.last_click_time = renpy.get_time()

        def handle_target_click(self, game):
            self.last_click_time = renpy.get_time()
            game.hit_target()

        def handle_background_click(self, game):
            game.miss_click()
            game.set_state(MissState())

        def update(self, game):
            if renpy.get_time() - self.last_click_time > 2.0:
                game.set_state(IdleState())

    # --- Miss state: short penalty after missing ---
    class MissState(ClickerState):
        def __init__(self):
            self.start_time = 0
            self.duration = 0.3

        def on_enter(self, game):
            self.start_time = renpy.get_time()

        def update(self, game):
            if renpy.get_time() - self.start_time > self.duration:
                game.set_state(IdleState())
init -90 python:
    class Gameroom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Gameroom",
                label_name = "gameroom",
                idle = "images/map/schoolmap/gameroom2/idle_gameroom.png",
                hover = "images/map/schoolmap/gameroom2/hover_gameroom.png",
                xpos = 980,
                ypos = 320
            )
            # create invoker and add command
            self.gameRoomInvoker = PredictionInvoker()
            self.gameRoomInvoker.commands.append(CallRoomCommand(self.label_name))

        def enter(self):
            # execute all commands
            self.gameRoomInvoker.executeCommands()
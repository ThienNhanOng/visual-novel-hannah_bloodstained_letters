init -90 python:
    class Gameroom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Gameroom",
                name = "Game Room",
                idle = "images/map/schoolmap/gameroom2/idle_gameroom.png",
                hover = "images/map/schoolmap/gameroom2/hover_gameroom.png",
                xpos = 980,
                ypos = 320,
                label_name = "gameroom"
            )
            # create command object
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            # execute the command (calls the label)
            self.command.execute()
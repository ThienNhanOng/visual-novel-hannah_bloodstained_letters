init -90 python:
    class CasinoRoom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Casino",
                label_name = "casinoroom",
                idle = "images/map/schoolmap/casino/idle_casino.png",
                hover = "images/map/schoolmap/casino/hover_casino.png",
                xpos = 51,
                ypos = 170
            )
            # create command object
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            # execute the command (calls the label)
            self.command.execute()
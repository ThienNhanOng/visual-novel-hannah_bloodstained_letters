init -90 python:
    class CourtyardRoom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Courtyard",
                label_name = "courtyardroom",
                idle = "images/map/schoolmap/courtyard/idle_courtyard.png",
                hover = "images/map/schoolmap/courtyard/hover_courtyard.png",
                xpos = 890,
                ypos = 700
            )

            # create command object
            self.command = CallRoomCommand(self.label_name, newScene=False)
            self.command = CallRoomCommand(self.label_name, newScene=False)
        def enter(self):
            # execute the command (calls the label)
            self.command.execute()
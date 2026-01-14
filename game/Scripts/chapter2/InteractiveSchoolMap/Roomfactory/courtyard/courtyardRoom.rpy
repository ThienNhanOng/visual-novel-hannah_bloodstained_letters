init -90 python:
    class CourtyardRoom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Courtyard",
                name = "Courtyard",           # ← fixed: use string, not variable
                idle = "images/map/schoolmap/courtyard/idle_courtyard.png",
                hover = "images/map/schoolmap/courtyard/hover_courtyard.png",
                xpos = 890,
                ypos = 700,
                label_name = "courtyardroom"
            )

            # create command object
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            # execute the command (calls the label)
            self.command.execute()
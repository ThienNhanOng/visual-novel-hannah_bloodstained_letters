init -90 python:
    class DormRoom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Dorm",
                label_name = "dormroom",
                idle = "images/map/schoolmap/dorm/idle_dorm.png",
                hover = "images/map/schoolmap/dorm/hover_dorm.png",
                xpos = 590,
                ypos = 600
            )
            # create command object
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            # execute the command (calls the label)
            self.command.execute()
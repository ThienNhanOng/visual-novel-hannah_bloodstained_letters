init -90 python:
    class TrackRoom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Trackroom",
                name = "Track Field",
                idle = "images/map/schoolmap/trackfield/idle_track.png",
                hover = "images/map/schoolmap/trackfield/hover_track.png",
                xpos = 450,
                ypos = 50,
                label_name = "trackroom"
            )
            # create command object
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            # execute the command (calls the label)
            self.command.execute()
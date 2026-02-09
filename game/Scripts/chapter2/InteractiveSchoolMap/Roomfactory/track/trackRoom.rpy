init -90 python:
    class TrackRoom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Trackroom",
                label_name = "trackroom",
                idle = "images/map/schoolmap/trackfield/idle_track.png",
                hover = "images/map/schoolmap/trackfield/hover_track.png",
                xpos = 450,
                ypos = 50
            )
            # create invoker and add command
            self.trackInvoker = PredictionInvoker()
            self.trackInvoker.commands.append(CallRoomCommand(self.label_name))

        def enter(self):
            # execute all commands
            self.trackInvoker.executeCommands()
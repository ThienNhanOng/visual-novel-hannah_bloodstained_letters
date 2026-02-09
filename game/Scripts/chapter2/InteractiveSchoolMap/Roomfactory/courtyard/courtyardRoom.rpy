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

            # create invoker and add command
            self.CourtyardInvoker = PredictionInvoker()
            self.CourtyardInvoker.commands.append(CallRoomCommand(self.label_name))
    
        def enter(self):
            # execute all commands
            self.CourtyardInvoker.executeCommands()
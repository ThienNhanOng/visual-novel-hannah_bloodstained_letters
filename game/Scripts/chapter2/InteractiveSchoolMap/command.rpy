#init -90 python:
init -100 python:
    # Command interface
    class RoomCommand:
        def execute(self):
            pass

    ##use command pattern to call the room
    class CallRoomCommand(RoomCommand):
        def __init__(self, label_name, newscene=True):
            self.label_name = label_name
            self.newscene = newscene

        #uses renpy call function to execute the room label
        def execute(self):
            if self.newscene:
                renpy.call_in_new_context(self.label_name)
            else:
                renpy.call(self.label_name)
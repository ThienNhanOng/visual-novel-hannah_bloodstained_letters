#init -90 python:
init -100 python:
    # Command interface to enter a room
    class RoomCommand:
            pass

    ##use command pattern to call the room
    class CallRoom(RoomCommand):
        def __init__(self, label_name, newscene=True):
            self.label_name = label_name
            self.newscene = newscene

        #entering the room if its a new call using renpy
        def execute(self):
            if self.newscene:
                renpy.call_in_new_context(self.label_name)
            else: #enter existing scene with current state
                renpy.call(self.label_name)
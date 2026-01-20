init -90 python:
    class CallRoomCommand(CommandInterface):

        def __init__(self, labelName, newScene=True):
            self.labelName = labelName
            self.newScene = newScene

        #the command uses renpy method to enter the label
        def execute(self):
            if self.newScene:
                renpy.call_in_new_context(self.labelName)
            else:
                #if not a new scene, just call normally
                renpy.call(self.labelName)
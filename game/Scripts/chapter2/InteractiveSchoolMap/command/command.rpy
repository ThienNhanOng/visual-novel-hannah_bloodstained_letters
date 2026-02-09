init -90 python:
    #inherit command interface 
    class CallRoomCommand(CommandInterface):

        def __init__(self, labelName, newScene=True):
            self.labelName = labelName
            self.newScene = newScene

        #the command uses renpy method to enter the label
        def execute(self):
            renpy.call(self.labelName)
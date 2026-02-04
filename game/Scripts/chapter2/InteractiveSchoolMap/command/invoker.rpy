
init -90 python:
    #invoke the command
    class PredictionInvoker:
        #initialize space for commands
        def __init__(self, commands=None):
            if commands:
                #pass existing commands
                self.commands = commands
            else:
                #if its a new command, create space for it
                self.commands = []

        #execute the command
        def executeCommands(self):
            for command in self.commands:
                command.execute()
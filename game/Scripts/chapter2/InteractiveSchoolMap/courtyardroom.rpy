#creating the room
#
image bg courtyard = "images/map/schoolmap/bg room1.png"

init -90 python:
    #define the courtyard room using factory pattern
    class CourtyardRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Courtyard",
                name="Courtyard",
                idle="images/map/schoolmap/courtyard/idle_courtyard.png",
                hover="images/map/schoolmap/courtyard/hover_courtyard.png",
                xpos=890,
                ypos=700,
                label_name="courtyardroom"
            )

            #use command pattern to call the room
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            self.command.execute()

    addroom(CourtyardRoom())


label courtyardroom:
    scene bg courtyard

    #run event handler
    call eventQueue

    #increase time after leaving the room
    $ timeIncrease()

    jump schoolmap
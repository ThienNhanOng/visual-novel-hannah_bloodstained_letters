#creating the room
#
init -90 python:
    # define the courtyard room using factory pattern
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
            renpy.call_in_new_context(self.label_name)

    addroom(CourtyardRoom())


    #placeholder test
label courtyardroom:
    scene bg room1
    "welcome to the courtyard"
    
    #menu: clean up the courtyard for money
    #attend class
    #talk to silas or on weekends, to 

    jump schoolmap
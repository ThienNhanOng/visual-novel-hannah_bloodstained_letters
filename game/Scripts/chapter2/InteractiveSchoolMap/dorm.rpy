#creating the room
#
init -90 python:
    #`Room` and `register_room` are defined earlier (see schoolMapFactory.rpy, init -100).
    class DormRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Dorm",
                name="Dorm",
                idle="images/map/schoolmap/dorm/idle_dorm.png",
                hover="images/map/schoolmap/dorm/hover_dorm.png",
                xpos=590,
                ypos=600,
                label_name="dormroom"
            )

            #use command pattern to call the room
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            self.command.execute()

    addroom(DormRoom())

#placeholder test
label dormroom:
    scene bg room1
    "You are in your dorm room."

    #Sleep is allowed at Night (2) or Bedtime (3).
    if timeIndex < 2:
        "It's not bedtime yet. Come back at night."
    else:
        "You go to sleep..."
        $ advancedNextDay()
        "You wake up on [currentDayLabel()] - [currentTime()]."

    jump schoolmap
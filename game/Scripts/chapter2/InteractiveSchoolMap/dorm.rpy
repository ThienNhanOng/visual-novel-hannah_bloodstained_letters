#creating the room
#
init -90 python:
    # `Room` and `register_room` are defined earlier (see schoolMapFactory.rpy, init -100).
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
            self.command = CallRoom(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(DormRoom())

#placeholder test
label dormroom:
    scene bg room1
    "welcome to the dorm"
    jump schoolmap
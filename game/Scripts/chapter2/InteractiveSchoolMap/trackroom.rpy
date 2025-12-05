#creating the room
#
init -90 python:
    # `Room` and `register_room` are defined earlier (see schoolMapFactory.rpy, init -100).
    class TrackFieldRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Trackroom",
                name="Track Field",
                idle="images/map/schoolmap/trackfield/idle_track.png",
                hover="images/map/schoolmap/trackfield/hover_track.png",
                xpos=450,
                ypos=50,
                label_name="trackroom"
            )

            #use command pattern to call the room
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(TrackFieldRoom())

#the room

#placeholder test
label trackroom:
    scene bg room1
    "welcome to the track"
    jump schoolmap

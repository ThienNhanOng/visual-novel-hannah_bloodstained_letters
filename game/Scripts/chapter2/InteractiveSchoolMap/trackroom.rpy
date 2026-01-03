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
            self.command = CallRoom(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(TrackFieldRoom())

default raisesCounter = 10
default payout = 15

#the room

#placeholder test
label trackroom:
    scene bg room1
    "welcome to the track"
    #increase time after leaving the room

    $ current_time = currentTime()

    if current_time == "Morning":
        Silas "exercising before class?"
    elif current_time == "Noon":
        $ SideChar = Character("Nearby Professor", color="#5c3304")
        SideChar "welcome to work! grab a rake"
        Player "on it!"
        "you made $[payout] for raking the leaves"
        play movie "videos/rake.mp4"
        $ Global_Money += payout
        $ raisesCounter += 1

        #will increase money by 1 each time you get a raise
        if raisesCounter > payout:
            $ payout += 1

    $ timeIncrease()
    jump schoolmap

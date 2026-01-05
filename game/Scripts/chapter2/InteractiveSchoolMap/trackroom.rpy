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

image bg room2 = "images/map/schoolmap/bg room2.png"

#the room

#placeholder test
label trackroom:
    scene bg room2
    "welcome to the track"
    #increase time after leaving the room

    $ current_time = currentTime()

    if current_time == "Morning":
        Silas "exercising before class?"

    
    elif current_time == "Noon" and purchased_items.get("ITEM2", False):
        $ SideChar = Character("Coach Paige", color="#5c3304")
        SideChar "Just in time! and welcome to work! grab a rake"
        Player "on it!"
        
        play movie "visualAnimation/raking.webm"
        "you made $[payout] for raking the leaves"
        $ Global_Money += payout
        $ raisesCounter += 1
    else:
        $ SideChar = Character("Coach Mark", color="#d3661d")
        SideChar "Hey! excuse me but please get off the track field"
        SideChar "this time is reserved for cleaning"

    #will increase money by 1 each time you get a raise
    if raisesCounter > payout:
        $ payout += 1
    if raisesCounter == 20:
        SideChar "great job! by the way you should enjoy your time here at school"
        SideChar "here take this if you go to the bookstore youll be able"
        SideChar "to buy a pass to the gameroom. it should help you relax"
        $ Global_Money += 10
        $ arcadeUnlocked = True
        "You unlocked access to the gameroom!"   
    $ timeIncrease()
    jump schoolmap

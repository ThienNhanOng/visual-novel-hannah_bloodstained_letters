#creating the room
#
image bg courtyard = "images/map/schoolmap/bg room1.png"

label courtyardroom:
    scene bg courtyard

    #run event handler
    call eventQueue

    #increase time after leaving the room
    $ timeIncrease()

    jump schoolmap
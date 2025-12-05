#creating the room
#
init -90 python:
    # `Room` and `register_room` are defined earlier (see schoolMapFactory.rpy, init -100).
    class ShopRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Shop",
                name="Shop",
                idle="images/map/schoolmap/shop1/idle_shop.png",
                hover="images/map/schoolmap/shop1/hover_shop.png",
                xpos=640,
                ypos=300,
                label_name="shoproom"
            )

            #use command pattern to call the room
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(ShopRoom())

#placeholder test
label shoproom:
    scene bg room1
    "welcome to the shop"
    jump schoolmap
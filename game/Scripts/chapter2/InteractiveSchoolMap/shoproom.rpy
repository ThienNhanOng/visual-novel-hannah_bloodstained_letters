#creating the room
#
init python: #dont need init -90 again since already in python block

    # define the shop room using factory pattern
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
            self.command = CallRoom(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(ShopRoom())

#first visit tracking
default first_visit_shop = False

#placeholder test
label shoproom:
    scene bg room1
    $ SideChar = Character("Sage", color="#5c3304")
    
    if first_visit_shop == False:
        SideChar "welcome to the Community Store!"
        SideChar "my name is Sage. I also run the journalist club!"
    else:
        SideChar "welcome back to the Community Store!"
    call screen Shopscreen


    jump schoolmap
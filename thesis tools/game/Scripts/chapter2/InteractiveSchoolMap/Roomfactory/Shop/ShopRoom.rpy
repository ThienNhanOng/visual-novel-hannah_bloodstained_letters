init -90 python:
    class ShopRoom(Room, Enterable):
        def __init__(self):
            super().__init__(
                room_id = "Shop",
                label_name = "shoproom",
                idle = "images/map/schoolmap/shop1/idle_shop.png",
                hover = "images/map/schoolmap/shop1/hover_shop.png",
                xpos = 640,
                ypos = 300
            )
            # create command object
            self.command = CallRoomCommand(self.label_name, newScene=False)

        def enter(self):
            # execute the command (calls the label)
            self.command.execute()
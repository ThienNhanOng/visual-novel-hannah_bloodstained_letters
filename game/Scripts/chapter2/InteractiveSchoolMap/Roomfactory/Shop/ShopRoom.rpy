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
            # create invoker and add command
            self.shopInvoker = PredictionInvoker()
            self.shopInvoker.commands.append(CallRoomCommand(self.label_name))

        def enter(self):
            # execute all commands
            self.shopInvoker.executeCommands()
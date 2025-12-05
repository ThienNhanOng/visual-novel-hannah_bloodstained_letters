#creating the room
#
init -90 python:
    # define the casino room using factory pattern
    class CasinoRoomDef(Room):
        def __init__(self):
            super().__init__(
                room_id="Casino",
                name="Casino",
                idle="images/map/schoolmap/casino/idle_casino.png",
                hover="images/map/schoolmap/casino/hover_casino.png",
                xpos=51,
                ypos=170,
                label_name="CasinoRoom"
            )

            #use command pattern to call the room
            self.command = CallRoomCommand(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(CasinoRoomDef())

#placeholder test
label CasinoRoom:
    scene expression im.Scale("blackjack/background.jpeg", config.screen_width, config.screen_height)
    "welcome to the casino"
    play music "Scripts/chapter2/jumping_game/ninja racer stuff/Pixel Highway.wav" loop
    call screen blackjack_table
    stop music fadeout 2.0

    if(result == "win"):
        $ Global_Money += player_money
    
    elif(result == "lose"):
        $ Global_Money -= player_money
    else: 
        $ Global_Money = player_money
        

    jump schoolmap
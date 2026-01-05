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
            self.command = CallRoom(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(CasinoRoomDef())

#placeholder test
label CasinoRoom:
    scene expression im.Scale("blackjack/background.jpeg", config.screen_width, config.screen_height)
    "welcome to the casino"
    play music "Scripts/chapter2/jumping_game/ninja racer stuff/Pixel Highway.wav" loop
    
    #first check: only available at night
    if currentTime() == "Night":
        "Please enjoy your stay"
        #check if player has fake ID
        if purchased_items.get("ITEM1", False):
            $ playerMoney = Global_Money
            call screen blackjack_table
            stop music fadeout 2.0

            if(result == "win"):
                $ Global_Money += playerMoney
            
            elif(result == "lose"):
                $ Global_Money -= playerMoney
            else: 
                $ Global_Money = playerMoney
            
            $ timeIncrease()

        else:
            "wait actually...can I see your ID?"
            Player "i don't have one..."
            "Sorry, you need an ID to enter the establishment."
            "Please come back later with an ID."
            $ timeIncrease()
    else:
        "The casino is currently closed. Please come back at night."
    jump schoolmap
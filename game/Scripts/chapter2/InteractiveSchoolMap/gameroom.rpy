#creating the gameroom with the factory.
#
init -90 python:
    class GameRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Gameroom",
                name="Game Room",
                idle="images/map/schoolmap/gameroom2/idle_gameroom.png",
                hover="images/map/schoolmap/gameroom2/hover_gameroom.png",
                xpos=980,
                ypos=320,
                label_name="gameroom"
            )

            #use command pattern to call the room
            self.command = CallRoom(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(GameRoom())

#placeholder test
label gameroom:
    
    scene blackscreen 
    stop music fadeout 2.0
    "welcome to the game room"
    
    menu:
        "Do you want to play?"
        "Yes (cost $10)":
            if Global_Money >= 10:
                $ Global_Money -= 10
                $ jump_score = 0  # Reset score for new game
                $ game = None  # Will be initialized below

                # Initialize game safely
                $ game = SimpleGameState()

                play music "Scripts/chapter2/jumping_game/ninja racer stuff/Pixel Highway.wav" fadein 10.0 loop

                call screen jump_game
                stop music fadeout 2.0
                #reward player money 
                $ Global_Money += int(round(jump_score / 100.0) * 10)  # Convert 100 points = 10 dollars
                jump lostscreen
            else:
                "You need at least $10 to play."
        #if no   
        "no":
            "What a shame. Maybe next time."
    #increase time after leaving the room
    $ timeIncrease()
    
    jump schoolmap
#placeholder test
label casinoroom:
    #from .package import Room      
    #from .interface import Enterable
    scene expression im.Scale("blackjack/background.jpeg", config.screen_width, config.screen_height)
    "welcome to the casino"
    play music "Scripts/chapter2/jumping_game/ninja racer stuff/Pixel Highway.wav" loop
    
    #first check: only available at night
    if currentTime() == "Night":
        "Please enjoy your stay"
        #check if player has fake ID
        if purchased_items.get("fake_id", False):
            $ playerMoney = Global_Money
            call screen blackjack_table
            stop music fadeout 2.0

            # Sync money back - blackjack already handled wins/losses
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

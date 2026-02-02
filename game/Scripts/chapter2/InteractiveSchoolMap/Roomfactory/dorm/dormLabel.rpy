#creating the room
#
#placeholder test
label dormroom:
    show mcsleep
    "You are in your dorm room."
    
    if hiddenletterUnlocked == True and purchased_items.get("hiddenletter", False) == False:
        if hiddenletterUnlocked and purchased_items.get("letter", False):
            $ Theo_counter = Silas_counter + 1
            show situp
            "life has been so strange lately..."
            "I couldnt sleep. I keep remenecing about Hannah"
            "I remember the mentioning that the school may have some connection to her."
            "but do i really want to know?"
            "Just as i felt as if I moved on?"
            Player "maybe I should look around the dorm a bit more."
            jump investigating_the_school

    # Sleep is allowed at Night (2) or Bedtime (3).
    if timeIndex < 2:
        "you lay in bed but can't seem to fall asleep."
        "It's not bedtime yet. You got back up."
    else:
        "You go to sleep..."
        show mcsleep2
        $ advancedNextDay()
        "You wake up on [currentDayLabel()] - [currentTime()]."
    hide mcsleep2
    hide mcsleep
    jump schoolmap


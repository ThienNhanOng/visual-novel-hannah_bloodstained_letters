#creating the room
#
#placeholder test
label dormroom:
    show mcsleep
    "You are in your dorm room."
    
    
    # Sleep is allowed at Night (2) or Bedtime (3).
    if timeIndex < 2:
        "you lay in bed but can't seem to fall asleep."
        "It's not bedtime yet. You got back up."
    else:
        "You go to sleep..."
        show mcsleep2
        $ advancedNextDay()
        "You wake up on [currentDayLabel()] - [currentTime()]."
    jump schoolmap
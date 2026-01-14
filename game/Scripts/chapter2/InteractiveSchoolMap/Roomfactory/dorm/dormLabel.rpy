#creating the room
#
#placeholder test
label dormroom:
    scene bg room1
    "You are in your dorm room."

    #Sleep is allowed at Night (2) or Bedtime (3).
    if timeIndex < 2:
        "It's not bedtime yet. Come back at night."
    else:
        "You go to sleep..."
        $ advancedNextDay()
        "You wake up on [currentDayLabel()] - [currentTime()]."

    jump schoolmap
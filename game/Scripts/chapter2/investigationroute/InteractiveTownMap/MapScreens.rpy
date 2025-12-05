# Initialize map decision counter
default MapDecision_counter = 0
default mapDecisionDetectivefirstEncounter = False
default mapDecisionMiafirstEncounter = False
default mapDecisionGTfirstEncounter = False
# Label to show the map
label MapScreens:
    play music "audio/MusicAndSoundtracks/map_exploration_theme.mp3" fadein 1.0 loop
    show screen MapScreen
    return  # returns control to whatever called MapScreens

# Map screen definition
screen MapScreen:
    add "images/map/townmap/TownmapPlaceholderBackup.png"

    # Button for Mia's house
    imagebutton:   
        xpos 728    
        ypos 360
        idle "images/map/townmap/IdleMiaRoom.png"
        hover "images/map/townmap/HoverMiaRoom.png"
        action Function(renpy.call, "InteractiveMiaRoom")

    # Button for GT Jewelry
    imagebutton:
        xpos 1674
        ypos 440
        idle "images/map/townmap/IdleGTJewelerly.png"
        hover "images/map/townmap/HoverGTJewelerly.png"
        action Function(renpy.call, "InteractiveGTRoom")

    # Vertical part (left of hole) – Forest Room
    imagebutton:
        xpos 46
        ypos 488
        xsize 354       # 400 - 46
        ysize 564       # 1052 - 488
        idle "images/map/townmap/IdleForestRoom.png"
        hover "images/map/townmap/HoverForestRoom.png"
        action Function(renpy.call, "InteractiveForestRoom")

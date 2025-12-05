
# Label to show the map
label schoolmapScreen:
    show screen schoolmapScreen
    return  # returns control to whatever called this label

# Map screen backup
screen schoolmapScreen:
    # Robust background load with fallback + on-screen debug
    if renpy.loadable("images/map/schoolmapbackup.png"):
        add "images/map/schoolmapbackup.png"
    elif renpy.loadable("images/map/schoolmap/schoolmap.png"):
        add "images/map/schoolmap/schoolmap.png"
    elif renpy.loadable("images/map/schoolmap/schoolmap.jpg"):
        add "images/map/schoolmap/schoolmap.jpg"
    else:
        add Solid("#222")
        text "Missing: images/map/schoolmapbackup.png or schoolmap.(png/jpg)" xalign 0.5 yalign 0.5
    
    for room in SchoolmapRooms.values():
        # Only create a button if an idle image is provided
        if room.idle:
            imagebutton:
                xpos room.xpos
                ypos room.ypos
                idle room.idle
                hover room.hover
                action Function(room.command.execute)

    #wallet and dates ui
    $ wallet_ui = "images/wallet.png"
    add wallet_ui xpos 1400 ypos 0 xsize 550 ysize 250
    text "$$: [Global_Money]" size 60 xpos 1590 ypos 130 color "#000000"
    text "day" size 60 xpos 1470 ypos 83 color "#000000"
    

screen schoolMapScreen():
    use schoolmapScreen


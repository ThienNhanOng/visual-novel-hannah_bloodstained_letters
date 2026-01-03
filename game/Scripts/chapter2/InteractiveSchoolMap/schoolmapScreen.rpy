
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
            # Check if it's bedtime and not the dorm room
            $ is_night = currentTime() == "Bedtime"
            $ is_dorm = room.room_id == "Dorm"
            $ can_enter = not is_night or is_dorm
            
            imagebutton:
                xpos room.xpos
                ypos room.ypos
                idle room.idle
                hover room.hover
                action If(can_enter, Function(room.command.execute), Show("night_restriction_popup"))

    #wallet and dates ui
    $ wallet_ui = "images/wallet.png"
    add wallet_ui xpos 1400 ypos 0 xsize 550 ysize 250
    text "$$: [Global_Money]" size 60 xpos 1590 ypos 130 color "#0d4610"
    text "[current_day_label()]" size 60 xpos 1470 ypos 60 color "#000000"
    text "[currentTime()]" size 48 xpos 1440 ypos 125 color "#000000"
    

screen schoolMapScreen():
    use schoolmapScreen

# Popup screen for night time restriction
screen night_restriction_popup():
    modal True
    zorder 100
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        background "#000c"
        
        vbox:
            spacing 20
            text "It's too late at night!" size 32 xalign 0.5 color "#ff6b6b"
            text "Most facilities are closed.\nPlease return to your dorm." size 22 xalign 0.5
            textbutton "OK" action Hide("night_restriction_popup") xalign 0.5 text_size 24


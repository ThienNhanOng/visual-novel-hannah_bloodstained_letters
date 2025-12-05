## Screen with Stats Button
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action ShowMenu("mapUI")

label call_mapUI:
    call screen MapUI

screen MapUI:
    add "map/bg map.jpg"
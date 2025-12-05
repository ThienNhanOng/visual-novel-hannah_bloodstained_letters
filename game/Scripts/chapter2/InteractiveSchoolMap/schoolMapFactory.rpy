#init -100 debug because we need it to start way before anything else. caused errors interactive screenings
init -100 python:
    #defining the room default.
    class Room:
        def __init__(self, room_id, name, bg=None, idle=None, hover=None, xpos=0, ypos=0, label_name=None, flag_name=None):
            self.room_id = room_id #the name
            self.name = name #the visible name
            self.bg = bg #background image (may not used/overrided)
            self.idle = idle #for button idle state
            self.hover = hover #for button hover state
            self.xpos = xpos #x position on the map
            self.ypos = ypos #y position on the map
            self.label_name = label_name or room_id.lower() #label for the room
            self.flag_name = flag_name or f"{room_id}Visited" #check if it has been clicked on yet

    # global registry
    SchoolmapRooms = {}

    def addroom(room):
        # Add room
        SchoolmapRooms[room.room_id] = room
#room package for factory pattern
init -100 python:
    SchoolmapRooms = {}

    def addroom(room):
        if room is not None:
            SchoolmapRooms[room.room_id] = room

    class Room:
        def __init__(self, room_id, name, bg=None, idle=None, hover=None,
                    xpos=0, ypos=0, label_name=None, flag_name=None):
            self.room_id     = room_id
            self.name        = name
            self.bg          = bg
            self.idle        = idle
            self.hover       = hover
            self.xpos        = xpos
            self.ypos        = ypos
            self.label_name  = label_name or room_id.lower()
            self.flag_name   = flag_name or f"{room_id}Visited"

        def __repr__(self):
            return f"<Room {self.room_id}>"
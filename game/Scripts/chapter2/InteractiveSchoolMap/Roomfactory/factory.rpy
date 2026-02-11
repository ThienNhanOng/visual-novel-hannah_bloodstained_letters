#need base class to exist first
init -50 python:
    #factory to create the room for school map
    def create_room(roomType):
        #remove uppercases and spaces if I added any
        roomType = roomType.lower().strip()
        
        #key to match room to class
        roomTypes = {
            "casino": CasinoRoom,
            "courtyard": CourtyardRoom,
            "track": TrackRoom,
            "shop": ShopRoom,
            "gameroom": Gameroom,
            "dorm": DormRoom,
        }
        #return the room with the type of room it is.
        room = roomTypes.get(roomType)
        
        #instantiates the room if it exist
        if room:
            room = room()
            SchoolmapRooms[room.room_id] = room
        else:
            room = None

        return room 


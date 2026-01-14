init -50 python:
    # Option B: factory creates + auto-registers (cleaner in many cases)
    def create_room(roomType):
        roomType = roomType.lower().strip()
        room = None

        if roomType == "casino":
            room = CasinoRoom()
        elif roomType == "courtyard":
            room = CourtyardRoom()
        elif roomType == "track":
            room = TrackRoom()
        elif roomType == "shop":
            room = ShopRoom()
        elif roomType == "gameroom":
            room = Gameroom()
        elif roomType == "dorm":
            room = DormRoom()

        if room is not None:
            SchoolmapRooms[room.room_id] = room   # or call addroom(room)
        else:
            renpy.notify(f"Unknown room: {roomType}")

        return room 


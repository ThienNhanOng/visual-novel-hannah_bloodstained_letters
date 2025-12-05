#room subclasses using factory
init -90 python:

    # Courtyard Room
    class CourtyardRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Courtyard",
                name=room_id,
                idle="images/map/schoolmap/courtyard/idle_courtyard.png",
                hover="images/map/schoolmap/courtyard/hover_courtyard.png",
                xpos=890,
                ypos=700,
                label_name="courtyardroom"
            )

    # Cafeteria Room
    class CafeteriaRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Cafeteria",
                name=room_id,
                idle="images/map/schoolmap/cafeteria/idle_cafeteria.png",
                hover="images/map/schoolmap/cafeteria/hover_cafeteria.png",
                xpos=500,
                ypos=600,
                label_name="cafeteriaroom"
            )

    # Track Field Room
    class TrackRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Trackroom",
                name=room_id,
                idle="images/map/schoolmap/trackfield/idle_track.png",
                hover="images/map/schoolmap/trackfield/hover_track.png",
                xpos=450,
                ypos=50,
                label_name="trackroom"
            )

    # Shop Room
    class ShopRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Shop",
                name=room_id,
                idle="images/map/schoolmap/shop1/idle_shop.png",
                hover="images/map/schoolmap/shop1/hover_shop.png",
                xpos=640,
                ypos=300,
                label_name="shoproom"
            )

    # Casino Room
    class CasinoRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Casino",
                name=room_id,
                idle="images/map/schoolmap/casino/idle_casino.png",
                hover="images/map/schoolmap/casino/hover_casino.png",
                xpos=51,
                ypos=170,
                label_name="CasinoRoom"
            )

    # Game Room
    class Gameroom(Room):
        def __init__(self):
            super().__init__(
                room_id="Gameroom",
                name=room_id,
                idle="images/map/schoolmap/gameroom2/idle_gameroom.png",
                hover="images/map/schoolmap/gameroom2/hover_gameroom.png",
                xpos=980,
                ypos=320,
                label_name="gameroom"
            )

    # Dorm Room
    class DormRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Dorm",
                name=room_id,
                idle="images/map/schoolmap/dorm/idle_dorm.png",
                hover="images/map/schoolmap/dorm/hover_dorm.png",
                xpos=590,
                ypos=600,
                label_name="dormroom"
            )

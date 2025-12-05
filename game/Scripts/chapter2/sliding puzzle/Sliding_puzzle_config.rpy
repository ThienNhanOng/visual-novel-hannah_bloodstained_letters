# sliding_puzzle_config.rpy
# Configuration for the 9-tile sliding puzzle

# List of puzzle images
define puzzle_images = [
    "images/slidingpuzzle/game1/tile_1.png",
    "images/slidingpuzzle/game1/tile_2.png",
    "images/slidingpuzzle/game1/tile_3.png",
    "images/slidingpuzzle/game1/tile_4.png",
    "images/slidingpuzzle/game1/tile_5.png",
    "images/slidingpuzzle/game1/tile_6.png",
    "images/slidingpuzzle/game1/tile_7.png",
    "images/slidingpuzzle/game1/tile_8.png",
    #"images/slidingpuzzle/game1/tile_9.png",
    None  # This represents the blank 9th tile
]

# Winning image
define puzzle_complete_image = "images/slidingpuzzle/messy dormroom resized.png"
define Reward_image = "images/slidingpuzzle/organized dormroom.jpg"
# Puzzle grid size (3x3)
define puzzle_rows = 3
define puzzle_cols = 3

# -----------------------------------
# Backgrounds
# -----------------------------------

# Full-screen noir background
image BGnoir = "images/chapter1/forest scene/background/noir_background.jpg"

# Single lightning image (normal definition)
image BG_lightning = "images/chapter1/forest scene/background/lightning.jpg"
image BG_lightning_generic = "D:\renpyProject\Thesis Hannah Bloodstained letters\game\images\chapter1\forest scene\background\lightning_generic.jpeg"

# Define the animated background
image bg church_animated = Movie(
    play="images/chapter1/inside the church/bg_churchgif.mp4",
    size=(config.screen_width, config.screen_height)
)
#--------------------------------------------



# Characters

# Player images
image Player_L1 = "images/chapter1/forest scene/player/player right view.png"
image Player_L1Shadow = "images/chapter1/forest scene/player/player right view shadow.png"
image wallet_ui = "images/wallet.png"

init:
    image silas talk:
        "images/chapter1/forest scene/silas/silas_talk1.png"
        pause 0.5
        "images/chapter1/forest scene/silas/silas_talk2.png"
        pause 0.5
        repeat

# -----------------------------------
# Full Images / Overlays
# -----------------------------------

# Full-screen crowd funeral image
image crowd_funeral:
    "images/chapter1/forest scene/forest1.jpg"
    xysize (1920, 1080)  # Adjust to your game's resolution


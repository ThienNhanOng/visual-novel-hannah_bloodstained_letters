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
    xysize (config.screen_width, config.screen_height)

#-----------------------------------TALK BETWEEN MC AND silas-----------------------------------
image scene2bgSilas:
    "images/chapter1/interaction with silas/silastownbackground.jpeg"
    xysize (config.screen_width, config.screen_height)

image scene2bgSilasSit:
    "images/chapter1/interaction with silas/ch2silassit.png"
    xysize (config.screen_width, config.screen_height)
#-----------------------------------mc and detective-----------------------------------
image scene2detective1: #shadow image
    "images/chapter1/detective/detectivebgremoved.png"
    xysize (1655, 1150)
    xpos .93

image scene2detective2: #smoking middle image
    "images/chapter1/detective/detectivesmoking.png"
    xysize (1655, 1150)
    xpos .52

#overlay to talking detective
image detectivefaceleft: 
    "images/chapter1/detective/detectivefaceleft.png"
    xysize (400, 500)
    xpos .1
    #onlayer overlay cant be defined only called

image Player_L1overlay:
    "images/chapter1/forest scene/player/player right view.png"
    xysize (600, 350)
    xpos 0.15
    ypos 1.0

        
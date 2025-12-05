# this scene contain the flashback of when hanna severed arm and jawbone was found.
# 
#
#
default flashback_seen = False
image arm = im.Scale("images/chapter1/forest scene/background/minigame arm.jpeg", config.screen_width, config.screen_height)

label Chapter1Scene1Flashbacks:
    scene noir_background with fade
    centered "{color=#FFFFFF}{b}FLASHBACK XXX DAYS AGO{/b}{/color}"

    #stop music fadeout 1.0
    #play sound "flashback_whoosh.ogg"

    #image of town but this will make it desaturated/black and white
    
    #image townImage = im.MatrixColor("my_image.png", im.matrix.desaturate()) 
    #show townImage
    #scene bg BG_lightning 
    #show player
    show Player_L1 at left
    Player "Two weeks... and still no trace of the killer."
    Player "No footprints. No fingerprints. No trail. Nothing."
    hide Player_L1
    show Player_L1Shadow at left
    #show forensic team with a clipboard walking up
    #show forensic_team on the right side of the screen
    hide Player_L1Shadow
    show forensic2 at right

    $ SideChar = Character("Forensic Captain", color="#748649")
    SideChar "Excuse me, miss... you must be her sister."
    SideChar "Every test matches. I'm sorry, but it's your sister."
    SideChar "However, if you'd like you can inspect the remains yourself."
    hide forensic2
    hide noir_background
    scene arm

    #call mini game clicker 
    call clickergame
    hide arm
    show noir_background
    Player "I see. Thank you for your hard work."
    hide forensic2
    #show forensic1 at right
    
    SideChar "I do apologize."
    #
    hide forensic_team

return

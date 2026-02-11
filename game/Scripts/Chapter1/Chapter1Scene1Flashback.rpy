#this scene contain the flashback of when hanna severed arm and jawbone was found.
#
#
#
default flashback_seen = False
image arm = im.Scale("images/chapter1/forest scene/background/minigame arm.jpeg", config.screen_width, config.screen_height)

label Chapter1Scene1Flashbacks:
    scene noir_background with fade
    centered "{size=140}{color=#FFFFFF}{b}FLASHBACK XXX DAYS AGO{/b}{/color}{/size}"
    centered "{size=140}{color=#FFFFFF}{b}FORENSICS INVESTIGATION{/b}{/color}{/size}"

    #stop music fadeout 1.0
    #play sound "flashback_whoosh.ogg"

    #image of town but this will make it desaturated/black and white
    
    #image townImage = im.MatrixColor("my_image.png", im.matrix.desaturate()) 
    #show townImage
    #scene bg BG_lightning 
    #show player
    

    show Player_L1 at left
    Player "Two weeks... and still no trace of Hannah coming home. im starting to get worried."
    Player "After our parents passed away, it always been just me and her."
    Player "hm."
    hide Player_L1
    show Player_rightViewShadow at left
    "[Player] was walking walking into town. on the very edge of the forest"
    "she see a crowd gathered around something. curious, she walked closer to see what was going on."
    Player "I wonder what is going on here."
    
    #show forensic team with a clipboard walking up
    #show forensic_team on the right side of the screen
    hide Player_rightViewShadow
    show forensic2 at right

    $ SideChar = Character("Forensic Captain", color="#748649")
    SideChar "Excuse me, miss...can, Please step back."
    Player "Sure, is everything alright?"
    SideChar "I am unable to disclose any information at this time."
    
    "[Player] looked past her shoulder and saw a gory scene."
    hide forensic2
    show Player_shocked1
    Player "how awful."
    hide Player_shocked1
    $ SideChar = Character("Forensic member", color="#d6e7ac")
    #show forensic2 at right
    SideChar "Hey captain, I think we found something."

    "[Player] overhear the faint discussion between the forensic team members."
    

    $ SideChar = Character("Forensic member", color="#d6e7ac", what_size=whisperFont)
    SideChar "under the rubbish we found an arm and a letter"
    $ SideChar = Character("Forensic Captain", color="#748649" , what_size=whisperFont )
    SideChar "let me see."
    show redletter
    "The captain tried to forcefully open the letter."
    "The letter was sealed with a wax stamp and accidentally destroyed the contents inside."
    SideChar "Fuck. well that sucks."
    "the forensic captain pick the letter up from the ground"
    centered "{size=140}{color=#6E0F0F}{b}TO HA*NAH NH****. {/b}{/color}{/size}"
    SideChar "To Hannah .."
    "the envelop was too distorted to read."
    show Player_L1overlay onlayer overlay
    Player "Notices the bracelet. that our mom gave to hannah. It was one of a kind"
    show player_shocked2
    show Player_L1overlay onlayer overlay
    "[Player] Rushes through the crowd. and onto the scene."
    $ SideChar = Character("Forensic Captain", color="#748649" , what_size=talkFont )
    hide redletter
    hide player_shocked2
    show forensic2 at right

    SideChar "HEY! you can't be here!"
    Player "That is my sister im sure of it!"
    SideChar ".."
    SideChar "What is her name?"
    Player "Hannah. Hannah XXXXXXXX"
    "The detective look down at the envelope. and allowed [Player] through."
    SideChar "this was on her."
    "The captain handed her the letter."

    SideChar "Can you please verify if it really is your sister?"
    hide forensic2
    hide noir_background
    scene arm

    #call mini game clicker 
    "Instructions: click the axe as many times as you can with MB1."
    call clickergame
    hide arm
    show noir_background
    Player "It is her..."
    hide forensic2
    #show forensic1 at right
    
    SideChar "I do apologize."
    hide forensic_team

return

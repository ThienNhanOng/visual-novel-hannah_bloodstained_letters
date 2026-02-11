label Chapter1Scene1:
    play music "audio/MusicAndSoundtracks/nolyrics.mp3" loop


    #scene bg_forest with fade
    

    "It was a somber day. The wind whispered through the trees, sharp and unforgiving."
    "The ground, veiled in white, bore the shadows of those gathered."
    
    show crowd_funeral at center with dissolve
    centered "{i}{color=#FFFFFF}Here lies Hannah —\nBrave, kind, and endlessly devoted.\nGone too soon, never forgotten.{/color}{/i}"

    #Flashback starts
    if not flashback_seen:
        call Chapter1Scene1Flashbacks
        $ flashback_seen = True
    #Flashback ends

    centered "{size=140}{color=#FFFFFF}{b}FLASHBACK ENDS{/b}{/color}{/size}" with fade
    centered "{size=140}{color=#FFFFFF}{b}during Hannah's funeral.{/b}{/color}{/size}" 

    scene forest2
    Player "To my right, I notice a silhouette emerge from the edge of the forest."

    hide forest2
    #scale the image to fit screen
    scene expression im.Scale("images/chapter1/forest scene/background/lightning_generic.jpeg", config.screen_width, config.screen_height)
    show silas_sad at right with fade
    Silas "..."

    Player "Silas?\nIs that you?"
    hide silas_sad
    show silas_eyeview_sad at right
    "Silas looks at me with apologetic eyes. I turn away, distracting myself with the bed of roses on the ground."
    hide silas_eyeview_sad

    show silas talk at right

    Silas "Look, [Player]... I know this is hard to accept.\n but you been crying for days now. this isnt good for you."
    Silas "maybe it would be best if you let her go."
    Silas "I know it isn't fair of me to ask that. but if not for me then for Hannah. She wouldnt want to see you like this."

    hide silas talk
    #scene lightning.jpg (Repeat lighting causes error commented out for now)
    scene black with fade
    show player_angryfrontpov at center
    menu:
        "Response to Silas"
        "I got to figure out what happen to Hannah at the very least":
            Player "Listen sy, I know you mean well but I can't just give up on her."
            Player "At the very least. I need to figure out what happened to Hannah.\n to figure out who hurt her."
            Silas "that could be dangerous."
            Player "I KNOW."
            $ Silas_counter += 1
        "Hannah could be alive":
            $ Silas_counter += 1
            Player "I’m not ready to give up on Hannah."
            Player "I know all the evidence points to her vanishing but i cant accept that."
            Player "what if..."
            Player "what if she's still alive?"
        "Yes... given time.":
            Player "You're right. i'll be okay given time."

    hide player_angryfrontpov
    show silas_sad at right
    Silas "..."
    Silas "You know, I miss her too. She was like a sister to me as well."
    Silas "she used to bring us treats from the bakery all the time after work. I miss those days."

    Silas "hey, just know even if she's gone. you still have me. and other people who care about you."
    Player "like who?"
    Silas "well? there's Mia who's been Hannah's best friend. and look around. the whole town is here. not just for Hannah but for you."

    if Silas_counter == 1:
        Player "Thank you for being here."

    Player "I just can't believe she's gone. I feel so useless."

    hide silas_sad
    scene black with fade
    show silas_comfort
    "Silas places a hand on my shoulder, examining my dejected disposition."
    #Continue with church bell scene...
    "{i}[Player] and the mourners stood in silence, grief hanging heavy in the cold air. Soft sobs, whispered prayers, and the rustle of wind through trees were all that remained.{/i}"
    "{b}A sudden, sharp toll cuts through the stillness like a knife.{/b}"
    centered "{i}{b}One chime.{/b}{/i}"
    #play sounds of bell audio.
    play sound "audio/MusicAndSoundtracks/bell.wav"

    centered "{i}{b}Then another.{/b}{/i}"
    play sound "audio/MusicAndSoundtracks/bell.wav"

    centered "{i}{b}And another.{/b}{/i}"
    play sound "audio/MusicAndSoundtracks/bell.wav"

    Silas "We should head inside. The service is about to start."

    #player monologue
    ""

    Player "I stare at her headstone for awhile before heading in."
    Player "as i walk in I am trying to figuring out how I want to deliver the eulogy."

    Silas "Are you ready to walk into the reception?"

    menu:
        "Will you go to the reception?"
        "Yes":
            Player "Okay, let's go."
        "In a minute.":
            Player "I need a moment first."

    hide silas_comfort
    hide black

return

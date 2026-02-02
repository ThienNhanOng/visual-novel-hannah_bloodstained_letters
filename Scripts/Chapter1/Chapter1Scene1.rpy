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

    Silas "Look, [Player]... I know this is hard to accept.\nBut she's gone...\nAnd I get it, it's not fair of me to ask this of you."
    Silas "But for me...\nfor all of us...\nPlease, accept the funeral we've arranged for Hannah. She deserves a place to rest."
    Silas "..."
    Silas "Are you okay?"
    hide silas talk
    #scene lightning.jpg (Repeat lighting causes error commented out for now)
    scene black with fade
    show player_angryfrontpov at center
    menu:
        "Response to Silas asking if I am okay"
        "How can I be okay???":
            Player "How can I be okay???"
            Player "Hannah is out there! I know she is! And instead of preserving her arm, we are just burying it!"
            Silas "Enough!\nI know it’s hard, but you need to let her go. She wouldn’t want you to suffer like this."
            $ Silas_counter += 1
        "I am not ready to give up on Hannah.":
            $ Silas_counter += 1
            Player "I’m not ready to give up on Hannah."
        "Yes... given time.":
            Player "Yes... I'll be okay... given some time."

    hide player_angryfrontpov
    show silas_sad at right
    Silas "..."
    "He hesitates, seemingly regretting his question. He knows the pain I've been through, how many tears the death of my sister has brought me."

    Silas "I know it's not fair of me to ask that. I'm sorry.\nYou know, I still think about her a lot. Hannah was so kind."

    if Silas_counter == 1:
        Player "I'm sorry I lashed out at you."

    Player "I just can't believe she's gone. I feel so useless."

    hide silas_sad
    scene black with fade
    show silas_comfort
    "Silas places a hand on my shoulder, examining my dejected disposition."
    #Continue with church bell scene...
    "{i}The player and the mourners stood in silence, grief hanging heavy in the cold air. Soft sobs, whispered prayers, and the rustle of wind through trees were all that remained.{/i}"
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
    "It tears me apart. Everyone's already given up and decided Hannah is gone. {i}Dead{/i}."
    "And the worst part? We haven't even done the bare minimum to bring her justice."

    "And now... I'm expected to say my final goodbye."
    "I glance down at the bed of roses one last time—soft petals draped in sorrow, a silent farewell that feels far too soon."

    Silas "Are you ready to walk into the reception?"

    menu:
        "Will you go to the reception?"
        "Yes":
            Player "Okay, let's go."
        "No":
            Player "I need a moment first."

    hide silas_comfort
    hide black

return

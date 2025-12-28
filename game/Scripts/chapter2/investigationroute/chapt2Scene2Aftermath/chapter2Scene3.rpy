transform fade_out:
    alpha 1.0
    pause 2.0          # How long text stays fully visible
    linear 2.0 alpha 0.0  # Fade out over 2 seconds
label Chapter2Scene3_fishing:
    play audio "audio/MusicAndSoundtracks/audio [vocals].mp3" fadein 1.0
    "[Player] went to visit the woods."
    centered "She walked around but could not find a cabin."
    "She kept walking to no results."
    "However as she was about to give up, she bumped into the detective casually fishing."
    
    "And singing?"
    $Theo_counter += 2
    Player "I walk up to the detective. I paid no minds to his presence. afterall, it's a populated place that is open to the public."
    Player "A beautiful day isn't it detective?"
    Theo "It is indeed, [Player]. Just another day in the life of a detective."
    Player "uh. Life of a detective by fishing?"
    "Theo laughs lightly."
    Theo "Where silent prey await a hunter's cast."
    Player "*confuse by his weird wording as always* \n well what did this 'hunter' catch?"

    #theo hands me a rod and tell me to test the experience myself.
    ##add fishing mini game
    #
    #if i catch 3 fish detective will warn me of danger. otherwise tell me maybe leave the investigation to him.
    #and in the meantime, look more into yourself. 
    #this will reroute to mia and route towards the school peaceful route.
    window hide
    show text "The sleuth proclaims another curious find\nOf Mia’s tale, where whispers darkly bind." at fade_out
    pause 4.0
    hide text

    show text "Rumour doth speak—an ally lurks at school,\nWhich marks why jewels rest by merchant's jewel'd pool." at fade_out
    pause 4.0
    hide text
    window show


    centered "Theo grabbed his stuff and walked away like usual."
    Player "Man... REALLY want to kick your ass into this lake right now."
    "[Player] walks away, muttering under her breath."

    "Suddenly, [Player] got a call from Silas." 
    centered "Ringing..."
    "RING"
    "Silas: Hey, [Player]. I need your help with something. can you drop by the school?"
    jump Chapter2Scene4_helpingSilas
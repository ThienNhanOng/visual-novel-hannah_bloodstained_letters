label Chapter1Scene2:    
    #show silas picture


    #image animated_church = Movie(play="game/visualAnimation/bg_churchgif.webm", size=(1920,1080))

    play movie "visualAnimation/bg_churchgif.webm" 

    scene black with moveinright
    "I walk in with silas. up to the podium"
    Silas"Let me know if it gets to be too much for you."

    
    show podium with zoomin:
        xysize ((1920, 1080))
#player monologue
    stop music fadeout 1.0
    play music "audio/MusicAndSoundtracks/Through the Storm.mp3" loop
    "Silas has been my best friends since before I can remember. \n
    He's usual much less serious, always teasing and joking with me. 
    We walk inside to attend the funeral"
    #show image 1
    "I look around, taking in the sea of faces surrounding me. More people than I expected… 
    all here to give their blessings."

    #show a picture of her thinking

    "Hannah was truly loved" 
    "As I step further into the reception hall, I’m met with a wave of mixed expressions. Pity.Hope..Grief...Confusion." 

    "Each face tells its own story—some trying to be strong, others barely holding it together.
    Then, all at once, I’m surrounded. Hands on my arms, voices in my ears. A blur of condolences and apologies:"
    hide podium 
    show talking_to_willy with irisin
    $ SideChar = Character("Man", color="#5c3304")
    SideChar "She was such a light to be around."
    hide talking_to_willy
    
    show oldevelyn
    $ SideChar = Character("Woman", color="#c508c5")
    SideChar "If there’s anything you need…"
    hide oldevelyn

    show girl with irisin
    $ SideChar = Character("Little girl", color="#e4245d")
    SideChar "“big sis Hannah didn’t deserve this.”"
    hide girl with irisin
    
    show player_cry with fade
    "The words blend together, a fog of sympathy and sorrow."
    "I nod. I thank them. But I can barely hear anything over the ache in my chest."
    hide player_cry
    
    
    show expression im.Scale("images/chapter1/inside the church/detective_black.png", config.screen_width, config.screen_height)
    $ SideChar = Character("???", color="#ce1313", what_size=whisperFont)
    SideChar "I am terribly sorry for your loss. Hannah was one of my best employees."
    hide detective_black
    
    show expression im.Scale("images/chapter1/inside the church/woman_black.png", config.screen_width, config.screen_height) with fade
    $ SideChar = Character("Older Woman", color="#5c3304", what_size=talkFont)
    SideChar "Oh Hannah was such a lovely girl, I am so sorry for what happened to her."

    Player "{b}sigh...{/b} I suppose it is nice to see such a turnout. Despite not having a lot of family" 
    "Hannah still managed to make an impact in other's lives."  

    # start the funeral service
    label scene_funeral_speech_intro:

    scene blackscreen

    "The service starts and I take my seat up front with Mia and Silas."
    "One by one, people go up on the stage and share stories about Hannah."
    "I start to remember that it will be my turn soon. The base of my stomach starts to turn."
    

    $ SideChar = Character("Pastor Willie", color="#7c9609", what_size=yellFont)
    SideChar "{b}And next on the itinerary is Hannah's sister, [Player].{/b}" 
    show expression im.Scale("images/chapter1/inside the church/onstage.png", config.screen_width, config.screen_height) with fade

    SideChar "Please come up to the podium."

    

    show expression im.Scale("images/chapter1/forest scene/player/player right view.png", 900, 800) at left as player
    "I take a few steps toward the podium, still trembling."
    hide player
    show expression im.Scale("images/chapter1/forest scene/player/player right view.png", 900, 800) at center as player
    "I reach the center of the stage, feeling every eye on me."
    hide player
    show expression im.Scale("images/chapter1/forest scene/player/playerviewleft.png", 900, 800) at right as player2

    "I take a scan of the audience once I'm on stage and immediately feel my anxiety worsen."
    "I take one last look around to seek comfort in the familiar faces."
    hide player2
    scene expression im.Scale("images/chapter1/inside the church/speachbackground.jpeg", config.screen_width, config.screen_height) with fade
    "I notice Mia, who was Hannah's best friend her whole life."
    "Silas sitting in the front row."
    "And even the agent who is in charge of investigating."

    "I take a deep breath and start my speech."
    
    #call speech with voice over.
    menu optional_name:
        "choose a speech to give"
        "reflective and hopeful":
            $ Mia_counter += 1
            call Chapter1ReflectiveSpeech

        "determination and justice":
            $ Silas_counter += 1
            $ StoryDecision_Chapter1_Investigate = True
            call Chapter1JusticeSpeech

    "Counter: Mia | [Mia_counter] | Silas | [Silas_counter] | Theo | [Theo_counter]"
    "chapter decision made: [StoryDecision_Chapter1_Investigate]"

    #can be theo or silas influenced routes from here.
    $ Player = Character(name, color="#25ffed", what_size=talkFont)
    scene noir_background with zoomout
    Player "After the reception, I stepped outside. The air was cold—sharper than before.
    I needed a moment to breathe. To feel something other than grief."
    Player "The quiet hum of conversation inside faded behind me. Just the wind now… and my own thoughts."
    play music "audio/MusicAndSoundtracks/shadowclues.mp3" loop

    $ SideChar = Character("???", color="#140f0f", what_size=talkFont)
    SideChar "step" 
    $ SideChar = Character("???", color="#140f0f", what_size=yellFont)
    SideChar "step"
    $ SideChar = Character("???", color="#140f0f", what_size=talkFont)
    "a figure approaches from the alleyway "
    

    


    # THEO OVERRIDE – mystery route. skill influenced by clicker game
    # requires player to get a score of 10 or more in the minigame to trigger.
    if Theo_counter == 1:
        scene expression im.Scale("images/chapter1/detective/detectivewallLean.png", config.screen_width, config.screen_height) 
        "..."
        scene expression im.Scale("images/chapter1/detective/talking to her.png", config.screen_width, config.screen_height)
        SideChar "{b}Leah correct?{/b}."
        Player "yes... who are you?"
        SideChar "{b}I just wish to say, that was a wonderful speech{/b} [Player]."
        "I continue to sit and comfort myself."
        "I look up to see who I was confronted by."
        Player "why, thank you."
        SideChar "Lo, the heavens weep without mercy, eh?"
        Player "..."
        scene expression im.Scale("images/chapter1/forest scene/background/lightning_generic.jpeg", config.screen_width, config.screen_height)
        scene expression im.Scale("images/chapter1/detective background.jpg", config.screen_width, config.screen_height) with fade
        scene expression im.Scale("images/chapter1/forest scene/background/lightning_generic.jpeg", config.screen_width, config.screen_height)
        scene expression im.Scale("images/chapter1/detective background.jpg", config.screen_width, config.screen_height) with fade
        #SideChar "ah forgive me but clock's ticking and I must be going."
        Player "Confuse by the bazaarre interaction...I nod."


        SideChar "Ah forgive me for my idling lass."
        call chapter1Scene3_MysteryApproach #talks about the case
        call chapter1Scene3_MeetingTheo


    #if minigame fail to trigger, it is silas vs mia influences. 

    elif Silas_counter > Mia_counter: #silas influenced route still mystery focus
        "Suddenly silas emerges from the shadows."
        call chapter1Scene3SilasInteraction
        call chapter1Scene3_MeetingTheo
    # MIA – peaceful route initiation. mia can have 2 possible points 1 from minigame or 1 from speech.
    else: #silas <= mia 
        call chapter1scene3Peaceful
    #stop music fadeout 2.0
return


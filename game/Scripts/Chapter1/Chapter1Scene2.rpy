label Chapter1Scene2:    
    #show silas picture


    #image animated_church = Movie(play="game/visualAnimation/bg_churchgif.webm", size=(1920,1080))

    play movie "visualAnimation/bg_churchgif.webm"

    scene black with moveinright
    "I walk in with Silas, up to the podium."
    Silas "Let me know if it gets to be too much for you."

    show podium with zoomin:
        xysize ((1920, 1080))
#player monologue
    stop music fadeout 1.0
    play music "audio/MusicAndSoundtracks/Through the Storm.mp3" loop
    "Silas has been my best friend since before I can remember.\nHe's usually much less serious, always teasing and joking with me."
    "But today, he's quiet. which is understandable."
    #show image 1
    "I look around, taking in the sea of faces surrounding me. More people than I expected… 
    all here to give their blessings."

    #show a picture of her thinking

    "Hannah was truly loved" 
    "As I step further into the reception hall, I’m met with a wave of mixed expressions. Pity.Hope..Grief...Confusion." 

    "Each face tells its own story—some trying to be strong, others barely holding it together. Then, all at once, I’m surrounded. Hands on my arms, voices in my ears. A blur of condolences and apologies."
    hide podium
    "many of the town folks come up to me to offer their condolences."
    "It was a cultural respect that the town follows."
    show talking_to_willy
    $ SideChar = Character("Man", color="#5c3304")
    SideChar "She was such a light to be around. I’m so sorry for your loss."

    hide talking_to_willy

    show oldevelyn
    $ SideChar = Character("Woman", color="#c508c5")
    SideChar "If there’s anything you need... I’m here for you."
    SideChar "let me know if you need anything at all."
    hide oldevelyn

    show girl with irisin
    $ SideChar = Character("Little girl", color="#e4245d")
    SideChar "Big sis Hannah didn’t deserve this. I’m so sorry for your loss."
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
    SideChar "Oh, Hannah was such a lovely girl. I am so sorry for what happened to her."

    Player "{b}sigh...{/b} I suppose it is nice to see such a turnout, despite not having a lot of family."
    "Hannah still managed to make an impact in others' lives."

    #start the funeral service
    label scene_funeral_speech_intro:

    #scene blackscreen

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

    "I scan the audience once I'm on stage and immediately feel my anxiety worsen."
    "I take one last look around to seek comfort in the familiar faces."
    hide player2
    scene expression im.Scale("images/chapter1/inside the church/speachbackground.jpeg", config.screen_width, config.screen_height) with fade
    "I notice our old neighbor Mia, Hannah's best friend."

    "and Silas, my neighbor and best friend since childhood."

    "as well as some unfamiliar faces, such as a few forensic members and investigators."
    "as weird as it may be, I am still glad to see them here. I guess they cared about Hannah too."

    "I take a deep breath and start my speech."

    #call speech with voice over.
    menu a:
        "Choose a speech to give"
        "Reflective and hopeful":
            $ Mia_counter += 1
            call Chapter1ReflectiveSpeech

        "Determination and justice":
            $ Silas_counter += 1
            $ StoryDecision_Chapter1_Investigate = True
            call Chapter1JusticeSpeech

    "Counter: Mia | [Mia_counter] | Silas | [Silas_counter] | Theo | [Theo_counter]"
    "Chapter decision made: [StoryDecision_Chapter1_Investigate]"

    #can be Theo or Silas influenced routes from here.
    $ Player = Character(name, color="#25ffed", what_size=talkFont)
    scene noir_background with zoomout
    Player "After the long reception, I stepped outside for some air"
    
    "The air was cold. sharper than this morning. I took a breath and embraced a moment to breathe."
    Player "quiet. Just the wind now and my own thoughts."
    play music "audio/MusicAndSoundtracks/shadowclues.mp3" loop fadein 2.0

    $ SideChar = Character("???", color="#140f0f", what_size=talkFont)
    SideChar "step"
    $ SideChar = Character("???", color="#140f0f", what_size=yellFont)
    SideChar "step"
    $ SideChar = Character("???", color="#140f0f", what_size=talkFont)
    "A figure approaches from the alleyway."

    #THEO OVERRIDE – mystery route. Skill influenced by clicker game
    #Requires player to get a score of 10 or more in the minigame to trigger.
    if Theo_counter == 1:
        scene expression im.Scale("images/chapter1/detective/detectivewallLean.png", config.screen_width, config.screen_height)
        "..."
        scene expression im.Scale("images/chapter1/detective/talking to her.png", config.screen_width, config.screen_height)
        SideChar "{b}[Player], correct?{/b}"
        Player "Yes... who are you?"
        SideChar "{b}I just wish to say, that was a wonderful speech,{/b} [Player]."
        "I continue to sit and comfort myself."
        "I look up to see who I was confronted by."
        Player "Why, thank you."
        SideChar "Usually eulogies and speeches put me to slumber, but yours was quite captivating."
        SideChar "No disrespect I should add."
        "I look up and see that it has start to rain again."
        SideChar "Lo, the heavens weep without mercy, eh?"
        SideChar "Raining all week no break. The roads has been muddy and treacherous."
        Player "..."
        scene expression im.Scale("images/chapter1/forest scene/background/lightning_generic.jpeg", config.screen_width, config.screen_height)
        scene expression im.Scale("images/chapter1/detective background.jpg", config.screen_width, config.screen_height) with fade
        scene expression im.Scale("images/chapter1/forest scene/background/lightning_generic.jpeg", config.screen_width, config.screen_height)
        scene expression im.Scale("images/chapter1/detective background.jpg", config.screen_width, config.screen_height) with fade
        #SideChar "Ah, forgive me but clock's ticking and I must be going."
        Player "Confused by the bizarre interaction... I nod."
        scene redletter
        SideChar "Ah, forgive me for my idling, lass."
        call chapter1Scene3_MysteryApproach #talks about the case
        call chapter1Scene3_MeetingTheo

    #If minigame fails to trigger, it is Silas vs Mia influences.
    elif Silas_counter > Mia_counter: #Silas influenced route, still mystery focus
        "Suddenly, Silas emerges from the shadows."
        call chapter1Scene3SilasInteraction
        stop music fadeout 2.0
        play music "audio/MusicAndSoundtracks/redEnvelope.mp3" loop 
        call chapter1Scene3_MeetingTheo
    #MIA – peaceful route initiation. Mia can have 2 possible points: 1 from minigame or 1 from speech.
    else: #Silas <= Mia
        Mia "How are you holding up, [Player]?"
        Player "Fine."

        call chapter1scene3Peaceful
    #stop music fadeout 2.0
return


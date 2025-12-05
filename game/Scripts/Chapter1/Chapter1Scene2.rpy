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
    
    $ SideChar = Character("???", color="#ce1313", what_size=whisperFont)
    SideChar "I am terribly sorry for your loss. Hannah was one of my best employees."
    
    $ SideChar = Character("Older Woman", color="#5c3304", what_size=talkFont)
    SideChar "Oh Hannah was such a lovely girl, I am so sorry for what happened to her."

    Player "{b}sigh...{/b} I suppose it is nice to see such a turnout. Despite not having a lot of family" 
    "Hannah still managed to make an impact in other's lives."  

    # start the funeral service
    label scene_funeral_speech_intro:

    scene church_interior with fade

    "The service starts and I take my seat up front with Mia and Silas."
    "One by one, people go up on the stage and share stories about Hannah."
    "I start to remember that it will be my turn soon. The base of my stomach starts to turn."

    $ SideChar = Character("Pastor Willie", color="#7c9609", what_size=yellFont)
    SideChar "{b}And next on the itinerary is Hannah's sister, [Player].{/b}" 
    SideChar "Please come up to the podium."

    "My legs start shaking as I stand and make my way."
    "I take a scan of the audience once I'm on stage and immediately feel my anxiety worsen."
    "I take one last look around to seek comfort in the familiar faces."

    "I notice Mia, who was Hannah's best friend her whole life."
    "Silas sitting in the front row."
    "And even the agent who is in charge of investigating."

    "I take a deep breath and start my speech."

    menu optional_name:
        "choose a speech to give"
        "reflective and hopeful":
            $ Mia_counter += 1
            call Chapter1ReflectiveSpeech

        "determination and justice":
            $ Silas_counter += 1
            call Chapter1JusticeSpeech

    "Counter: Mia | [Mia_counter] | Silas | [Silas_counter] | Theo | [Theo_counter]"
    $ Player = Character(name, color="#25ffed", what_size=talkFont)
    Player "After the reception, I stepped outside. The air was cold—sharper than before.
    I needed a moment to breathe. To feel something other than grief."
    Player "The quiet hum of conversation inside faded behind me. Just the wind now… and my own thoughts."

    $ SideChar = Character("???", color="#140f0f", what_size=talkFont)
    SideChar "step" 
    $ SideChar = Character("???", color="#140f0f", what_size=yellFont)
    SideChar "step"
    $ SideChar = Character("???", color="#140f0f", what_size=talkFont)
    SideChar "{b}that was a wonderful speech{/b} [Player]."
    "I turn around to face the sudden approach."
    Player "why, thank you."

    if Mia_counter == 1 and Silas_counter == 0:
        #initiate peaceful route
        $ StoryDecision_Chapter1_Investigate = 1
        jump chapter1scene3Peaceful
    elif Silas_counter == 2:
        call chapter1Scene3SilasInteraction
        jump chapter1Scene3_MeetingTheo
        #initiate mystery focus route with silas secret interaction
    elif Mia_counter == 1 and Silas_counter == 1:
        #initiate mystery focus route
        call chapter1Scene3_MysteryApproach
        jump chapter1Scene3_MeetingTheo

    #stop music fadeout 2.0
return
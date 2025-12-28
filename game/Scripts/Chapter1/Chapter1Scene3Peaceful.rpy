#in this scene the detective does not get introduced.


label chapter1scene3Peaceful:
#summary this scene focus on transitioning the player to a peaceful route with her going to school and moving on with her life.
    play music "audio/MusicAndSoundtracks/TitleScreenTrack.mp3" fadein 1.0 loop
    Mia "but ya know, You're not invincible, kid... don't go getting yourself killed now."

    Player "Mia, not now please..."

    Mia "...no I don't think I can."

    Mia "Someone has to teach you that the world doesn't hand out kindness. You gotta take your space."
    "It is time to move on kid. I know it's hard, but you have to let her go."

    Player "WHAT DO YOU KNOW?!"

    Player "(breathing heavy, voice rising) You all gave up the second they found that arm. Just a damn arm! No trail, no evidence, no answers!
    They said it was hers, and everyone just... accepted it. Closed the case. Buried an empty casket. Moved on.
    What if she’s not dead? What if there is more to this?"

    # Gets cut off
    "Mia hugs [Player]"

    Mia "ENOUGH! You're not the only one that had Hannah around you your whole life. I did too."
    Mia "I know she's a strong one. She's the most gritty, assertive person I know. I want to believe she's still out there too."
    Mia "BUT THERE'S NOTHING. ABSOLUTELY. NOTHING WE CAN DO."
    $ Mia = Character("Mia", color="#ffb6c1", what_size=whisperFont)

    Mia "even if she is out there and hiding as you said. I doubt Hannah wants to be found."
    "[Player], nods in respond to respecting what Mia said."

    "I burst down crying while holding Mia's embrace."
    $ Mia = Character("Mia", color="#ffb6c1", what_size=talkFont)
    Mia "Here... let's go home."

    "Mia drives [Player] home."

    Mia "You know, maybe it's better if you take some time for yourself. Focus on being a kid. You're only what, 15-16?"

    menu:
        "Answer to mia asking about your age?"
        "I'm 17":
            $ StoryDecision_Chapter1_Schoolname = "highschool"
            Mia "Eh, close enough."
        "I'm 19":
            $ StoryDecision_Chapter1_Schoolname = "college"
            Mia "Wow, time sure flies. You're a big girl now."


    Mia "My point is I get it. You're angry. You're lost. But here's the thing 
    you're still young. You've got your whole life ahead of you. So why not make the best out of it?"

    Mia "Why not join Silas in school? enroll yourself in [StoryDecision_Chapter1_Schoolname] and maybe one day, move out of this town chase 
    something better." 

    Mia "You’ll make some friends along the way. And you will learn how to take care of yourself."
    "not just to survive, but to actually live."
    Mia "Hannah would want that for you."

    Player "."
    Player "..."
    Player ""
    Player ""
    Player "I'll think about it."

    "Mia and [Player] arrive at [Player]'s house."

    Mia "And here we are! And no matter what choice you decide, just remember: you have Hannah's stubbornness and fire in your blood. Don't let anyone dim it."

    "Mia drove off."




    "DEBUG NOTE: END OF CHAPTER1 SCENE3"
return

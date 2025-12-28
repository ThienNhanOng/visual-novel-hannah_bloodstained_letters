label Chapter1ReflectiveSpeech:
    #voice over start time
    stop music fadeout 1.0
    play music "audio/speech/speech2reflective.mp3" 
    #13 17
    "sigh...."
    play sound "audio/MusicAndSoundtracks/crowd_clapping.mp3"
    $ renpy.pause(15, hard=True)
    Player "My sister… was always so selfless."
    "I remember when prom came around, I told her not to worry about me going—money was tight." 
    #20-23
    "She never got to go herself, but she said it was important for me to experience it." 
    $ renpy.pause(2, hard=True)
    #33-39
    "She worked extra shifts just so I could have a dress… and a corsage."
    $ renpy.pause(2, hard=True)
    #40-46
    
    "She always put others first, always wanted me to hold onto childhood just a little longer."
    $ renpy.pause(2, hard=True)
    #46-58
    "She was strong when no one asked her to be. Brave when no one saw."
    "She barely got the chance to live her life… and yet, she gave it so freely."
    $ renpy.pause(2, hard=True)
    "My eyes well up and I begin to sniffle. I look at Mia again. She reassures me with a smile."
    play movie "visualAnimation/haleymoving.webm"
    $ Player = Character(what_size=whisperFont)
    Player "All I hope for is that I can make my sister proud."

    "There was a short pause."

    window hide
    centered "Thank you..."
    window show
    stop music fadeout 1.0
    play sound "audio/MusicAndSoundtracks/crowd_clapping.mp3"
    Mia "starts claping. [Player], that was beautiful. \n everyone start to clap."
    play sound "audio/MusicAndSoundtracks/crowd_clapping.mp3"
return
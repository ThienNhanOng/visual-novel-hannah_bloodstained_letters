label chapter1Scene3SilasInteraction:

    scene forest_evening with fade
    scene scene2bgSilas 

    Silas "Despite how I wish you don't pursue Hannah, knowing it'll get dangerous... you have my full support."

    Player "Thank you, Silas... really."

    Silas "Anytime."

    Player "And thank you for checking on me."

    Silas "Don’t tell anyone, but I only came outside because I thought I saw a snack table. Turns out it was just a wet soggy floral arrangement… very disappointing."

    Player "Pft. Some friend you are... and here I thought you had a heart."
    scene scene2bgSilasSit with dissolve
    Silas "Ha..."
    "..."

    Silas "Remember when we were kids? we used to climb trees and doorbell ditch houses."
    Player "Yeah... those were the days."
    Silas "and how Hannah always yell at us and make us go back and apologize."
    "Silas and I reminisce about our childhood memories for a moment."
    Silas "I miss those times. Life was simpler back then."

    Silas "Say it's getting late. Would it be okay if I walked you home?"
    Player "Sure... I would like that that."
    
    $ renpy.music.set_volume(0.0, channel="movie")
    play movie "visualAnimation/videowalkhome.webm"
    pause 3.0
    $ renpy.music.set_volume(0, channel="movie") #turn off audio
    play sound "audio/MusicAndSoundtracks/thundernoises.mp3"
    play sound "audio/MusicAndSoundtracks/thundernoises.mp3"
    
    scene forest2
    "Silas continues to escort me home. exiting the town and deep into the woods."
    Silas "Once youre home safe, try to get some rest."
    
    scene blackscreen

    centered "{color=#fff}Silas walked me to my house, gave me a soft nod, and then turned to leave toward his own.{/color}" with dissolve
    centered "{color=#fff}Before I could open my door, I was once again approached from behind.{/color}" with dissolve

    
    $ SideChar = Character("???", color="#263503", what_size=talkFont)
    SideChar "You are [Player] I presume?"
    scene expression im.Scale("images/chapter1/detective/home.jpeg", config.screen_width, config.screen_height)
    "I turned around to see the same mysterous man with the trench coat from earlier."
    
    #o
    show scene2detective1 with fade:
    #override values
        xysize (1200, 800)
        xpos 0.60  
        ypos .3  
    


    Theo "we've met before, haven't we?"
    hide scene2detective1

    show scene2detective1 with fade:
    #override values
        xysize (1350, 1300)
        xpos 0.10
        ypos 0.1 

    Theo "I am sorry to intrude but the name is Theo. Theo Harper Chapman, private investigator."
    hide scene2detective1 with fade
    
    #scene expression im.Scale("images/chapter1/detective/detectivewallLean.png", config.screen_width, config.screen_height) 
    show scene2detective2

    Player "and how can I help you?"

    Theo "on the contrary, it is I who can help you. I have information which may seek to your interest. ms [Player]."
    scene 
    hide scene2detective2 with fade
    
    scene expression im.Scale("images/chapter1/detective/detectivewallLean.png", config.screen_width, config.screen_height) 
    
    #jump chapter1Scene3_MeetingTheo
return
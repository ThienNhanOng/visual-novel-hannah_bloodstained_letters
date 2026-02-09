label ending:

    if hiddenletterUnlocked and purchased_items.get("letter", False):
        #story continues leading to theo being the mastermind
        show redletter
        "As she about to leave she saw something that caught her attention. an envelope like object."
        Player "what is this Sy?"
        play music "game/audio/MusicAndSoundtracks/TitleScreenTrack.mp3" fadein 3.0 loop
        Silas "to be honest, no clue. it looks like an envelope of some sort. but there is some sort of force"
        Silas "sap or resin that prevent me from opening it without damaging the content inside."
        Player "it looks like the seal can be broken there are some weird marks on it."
        Silas "it does doesnt it. i've tried but it wont budge."
        Player "hm.. let me give it a go."
        
        #if player win continue story otherwise redo scene
        $ tttplayerWin = False
        call screen TicTacToeScreen
        if tttplayerWin:
            "the stamp unravel and illuminate itself with red and glitter"
            Player "Hey look! i did it!"
            Silas "really? Lets see..."
            "Inside the envelope was another crusty crumbly piece of paper."
            "certificate of authenticity. gt auctions."
            "seller of the 'Conan that Ran' a red and precious gem: Hannah"
            "and bidder as well as new owner: mr Edward harper-Chapman"
            "..."
            play movie "visualAnimation/TitleScreenLoop.webm"
            play sound "game/audio/thundernoises.mp3"
            Player "Chapman? where have i ever heard that name before..."
            "chapman...chapman..."
            Player "chapman...GASP"
            show reveal with pixellate
            "THEODORE EDWARD HARPER-CHAPMAN..."
            Player "SILAS. I MUST GO IM SORRY."
            "player rushes out after realizing the name."
            "the detective may not just be a detective but "
            "the very person behind all of this."
            scene black
            $ Player = Character(what_size=whisperFont)
            Player "AND IM TAKING THIS WITH MEEEEE!"
            Silas "WAIT! hold on!"
            "[Player] Disappears out of the dormatory before Silas could intervine."
            scene black with Dissolve(2.0)

            $ MainMenu()
        else:
            #Restart scene if player lose. as well as ttt state
            "You lost."
            $ resetTTTGame()
            jump ending
    else:
        "As she about to leave to dismiss any rumors, she saw a brochure."
        "It was definitely one that belongs to {i}JT Jewelry{/i}."
        "he doesn't seem like the type that is interested in jeweleries"
        "odd..."
        Player "Sy what is this?"
        Silas "oh that? \n Mia was on campus earlier today. and she dropped it"
        Silas "Maybe she was promoting on campus or something"
        Player "hm.. i see"
        Player "well i better get going. see you later Sy!"

        #note cliff hanger ending planned heavily for ch 4. canceled due to time.
        scene black with fade
        centered "{size=50}note: This path wouldve ultimately lead to mia being framed. if the story continues on{/size}"
        centered "{size=50}note: if reached, please replay and make sure silas affection isnt higher than theo's.{/size}"
    
        
    'end of chapter 2'
    $ MainMenu()
    #end of chapter2. 
    #continuation chapter3 will include meeting back up with theo and discussing about her findings.
    #this will ultimately lead to chapter 3 and 4 where more notes will show up leading to the 
    #confrontation with the mystery man. 

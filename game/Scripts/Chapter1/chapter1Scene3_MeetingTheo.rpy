#introduce the first letter found. 

label chapter1Scene3_MeetingTheo:
    scene expression im.Scale("images/chapter1/detective/note1.png", config.screen_width, config.screen_height)
    
    #onlayer overlay allow text over the textbox ui
    show detectivefaceleft at right onlayer overlay
    Theo "I've been digging into Hannah's disappearance, and the evidence isn't as thin as it first appeared. There are too many missing pieces—puzzles, if you will—for this to be mere chance. And I believe I now hold the first."

    centered "{size=48}{color=#eee}Detective Theo reaches into his coat pocket and pulls out a slightly crumpled letter.{/color}{/size}"
    show detectivefaceleft at right onlayer overlay
    Theo "There is something I have discovered. Prior to the young lass's disappearance, it appears she was involved in a jewelry business of some sort."


    "I'm shocked. It's a picture of Hannah. And Mia... along with a letter"
    show detectivefaceleft at right onlayer overlay
    Theo "January 32nd, 1**5. Two signatures are present. one belonging to the unfortunate lass, and the other to whom you know as Mia."
    show detectivefaceleft at right onlayer overlay
    Theo "From what I can gather, this seems to concern a business event. An auction invitation, perhaps."
    show detectivefaceleft at right onlayer overlay
    Theo "It speaks of a rare pure rose-pink diamond pendant—one of a kind, with only two known to exist."
    
    
    show Player_L1overlay onlayer overlay
    Player "entails the existence of a rare pure rose pink diamond pendant, a one of a kind with only 2 known in existence."
    show Player_L1overlay onlayer overlay
    Player "Signed by Hannah and Mia."
    "As I read through the contents of the letter, a chilling realization dawns upon me."
    $ Player = Character(Player, color="#ffb6c1", what_size=yellFont)
    show Player_L1overlay onlayer overlay
    Player "WAIT!...January 32nd? That date doesn't exist!"
    $ Player = Character(Player, color="#ffb6c1", what_size=talkFont)
    show detectivefaceleft at right onlayer overlay
    Theo "Indeed. An oddity that raises questions about the sender's intent and state of mind."
    show detectivefaceleft at right onlayer overlay
    Theo "to start, I suggest you pay a visit to this G.T. Jewelers."
    show detectivefaceleft at right onlayer overlay
    Theo "And Mia, however be cautious of how riches devours."

    menu: 
        "what to do next?"
        "Ask Theo for more information":
            Player "Can you tell me more about this G.T Jewelery?"
            Theo "G.T. Jewelers is a high-end jewelry company, known for its exquisite craftmanship"
            "theo toss over a newspaper clipping"
            Theo "however, rumors has it each stone brings tragedy to it's owner."
            #pictures of newspaper clippings of the jewelry
            "record of the red ruby burning. 1655"
            "another reported case of a tragic patreon of G.T jewelers died from drowning. 1*62"
            "green emerald vanity. poisoning. 1770"
            Player "flip. flip. flip."
            Player "the list.... just goes on"
            $Theo_counter += 2 #max counter at this point: 4
        "Thank Theo and leave":
            Player "I never knew my sister worked at a jewelry place..."    
            $Theo_counter += 1 #max counter at this point: 3

    Player "Thank you for your hard work. and for sharing this with me."

    Theo "Why, of course, milady. And should you ever find yourself in need, don’t hesitate to contact me for my service—let this card be your beacon—a silent promise to answer your call."

    "He offers the business card with a warm, knowing smile and nod prior to leaving."
    Theo_counter += 1
return
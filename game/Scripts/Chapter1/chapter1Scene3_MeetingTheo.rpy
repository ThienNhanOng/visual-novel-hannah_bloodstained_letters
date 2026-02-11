label chapter1Scene3_MeetingTheo:
    scene expression im.Scale("images/chapter1/detective/note1.png", config.screen_width, config.screen_height)

    #onlayer overlay allows text over the textbox UI
    show detectivefaceleft at right onlayer overlay
    Theo "I've been digging into Hannah's disappearance, and the evidence isn't as thin as it first appeared. There are too many missing pieces in our game of chess."
    Theo "but mere chance if you will, I believe I have stumbled across the first played piece."
    show redletter
    centered "{size=104}{color=#f11}{b}Detective Theo reaches into his coat pocket and pulls out a slightly crumpled envelope.{/b}{/color}{/size}"
    show detectivefaceleft at right onlayer overlay
    Theo "There is something I have discovered. Prior to the young lass's disappearance, it appears she was involved in a jewelry business of some sort."
    Player "hm..."
    hide redletter
    "I open the contents. and inside was a letter and a picture."
    "I'm shocked. It's a picture of Hannah. and in the background it looks like Mia."

    show detectivefaceleft at right onlayer overlay
    Theo "January 32nd, 1**5. Two signatures are present: one belonging to the unfortunate lass. and the other; signed Mia."
    show detectivefaceleft at right onlayer overlay
    Theo "From what I can gather, this seems to concern a business event. An auction invitation, perhaps."
    show detectivefaceleft at right onlayer overlay
    Theo "It speaks of a rare, pure rose-pink diamond pendant—one of a kind, with only two known to exist."

    show Player_L1overlay onlayer overlay
    Player "It entails the existence of a rare, pure rose-pink diamond pendant, one of a kind with only two known in existence."
    show Player_L1overlay onlayer overlay
    Player "Signed by Hannah and Mia."
    "As I read through the contents of the letter, a chilling realization dawns upon me."
    $ Player = Character(Player, color="#ffb6c1", what_size=yellFont)
    show Player_L1overlay onlayer overlay
    Player "WAIT!...January 32nd? That date doesn't exist!"
    $ Player = Character(Player, color="#ffb6c1", what_size=talkFont)
    show detectivefaceleft at right onlayer overlay
    play sound "audio/thundernoises.mp3"
    Theo "Indeed. An oddity that raises questions about the sender's intent and state of mind."
    show detectivefaceleft at right onlayer overlay
    play sound "audio/thundernoises.mp3"
    Theo "To start, I suggest you pay a visit to this G.T. Jewelers."
    show detectivefaceleft at right onlayer overlay
    Theo "And Mia—however, be cautious as there is a saying. the heart has its own hunger."
    "overindulge in wealth but heed thy warning."
    Theo "True hunger cannot be abated."
    Theo "endulge and devour the aroma of wealth as you will, but causion as glutten approaches" 
    Theo "Misery comes with delectable cusines."


    menu:
        "What to do next?"
        "Ask Theo for more information":
            Player "Can you tell me more about this G.T. Jewelry?"
            play sound "audio/thundernoises.mp3"
            Theo "G.T. Jewelers is a high-end jewelry company, known for its exquisite craftsmanship."
            "Theo tosses over a newspaper clipping."
            Theo "However, rumor has it each stone brings tragedy to its owner."
            #pictures of newspaper clippings of the jewelry
            "Record of the red ruby burning, 1655."
            "Another reported case: a tragic patron of G.T. Jewelers died from drowning, 1*62."
            "Green emerald vanity. Poisoning. 1770."
            Player "Flip. Flip. Flip."
            Player "The list... just goes on."
            $Theo_counter += 2 #max counter at this point: 4
        "Thank Theo and leave":
            Player "I never knew my sister worked at a jewelry place..."
            $Theo_counter += 1 #max counter at this point: 3

    Player "Thank you for your hard work, and for sharing this with me."

    Theo "Why, of course, milady. And should you ever find yourself in need, don’t hesitate to contact me for my service—let this card be your beacon—a silent promise to answer your call."

    "He offers the business card with a warm, knowing smile and a nod before leaving."
    $ Theo_counter += 1
return
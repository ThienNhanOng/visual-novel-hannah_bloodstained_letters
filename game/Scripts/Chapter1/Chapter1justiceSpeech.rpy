label Chapter1JusticeSpeech:
    stop music fadeout 1.0
    play music "audio/speech/speech1revenge.mp3" fadein 1.0

    $ renpy.pause(15, hard=True)
    Player "My sister was my entire world."
    "Hannah... she always knew what to say."
    Player "She always knew how to comfort others."
    #29-40
    $ renpy.pause(1, hard=True)
    "I remember when we were kids, we took care of a stray cat we named Sunny."
    "However, our parents didn't let us keep her. On the contrary, my dad took a gun and put her down."
    #show Player crying
    $ renpy.pause(2, hard=True)
    "I was devastated. I was crying so hard I couldn't breathe. I couldn't do anything but grieve."
    "Hannah sat beside me for hours through that whole moment."
    #show audience
    $ renpy.pause(2, hard=True)
    Player "I know she has helped others too, as can be seen by the people here."

    Player "They are here today to pay their respects and show their love for Hannah."
    Player "And yet, for all the love she gave, life gave her so little in return."
    Player "Before last week, I was still convincing myself we’d find her."
    Player "That she’d come back home."
    $ renpy.pause(3, hard=True)
    Player "But now… now I have to accept this. Or at least, I am expected to."
    Player "But I know there is more to this story. And I refuse to accept that she's just gone and there's nothing we can do."
    "I pause and take a steady breath. My voice hardens, just a little."

    "I glance over at Silas, knowing that I’m ignoring his advice."
    $ Player = Character(what_size=yellFont)
    #show Player sob
    Player "{b}I vow to uncover the truth{/b}. The whole, unshakable truth—about what happened to my sister."
    "Whether it leads to justice for her death, or reveals a reason behind her disappearance,"
    $ renpy.pause(1, hard=True)
    Player "One way or another... I won’t rest until I know."

    "The room falls into a hush. Maybe the others didn’t grasp the full weight of my words, but to me, each syllable rang like a verdict."

    window hide
    centered "Thank you..."
    window show
    $ renpy.pause(1, hard=True)
    show silas_sad at left with fade
    play sound "audio/MusicAndSoundtracks/crowd_clapping.mp3"
    Silas "*starts clapping.*"
    "There were others who clapped too."
    hide silas_sad
    "But at that moment, for me, he was the only one that mattered."
    stop music
return
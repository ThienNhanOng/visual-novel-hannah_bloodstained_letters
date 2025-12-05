label chapter1Scene3SilasInteraction:

    scene forest_evening with fade

    Silas "Despite how I wish you don't pursue Hannah, knowing it'll get dangerous... you have my full support."

    Player "Thank you, Silas... really."

    Silas "Anytime."

    Player "And thank you for checking on me."

    Silas "Don’t tell anyone, but I only came outside because I thought I saw a snack table. Turns out it was just a floral arrangement… very disappointing."

    Player "Pft. Some friend you are... and here I thought you had a heart."

    Silas "Hahaha... Shall we walk home?"

    # Walking animation and transition
    scene road_night with dissolve
    with Pause(1.5)

    Silas "Once you're home... get some rest. I promise I'll continue to help you search for your sister, and assist you until you are content."

    Player "You don’t have to. I know, like everyone else, you don't believe she's still out there either."

    "Silas kept walking silently beside me."
    "Well... she ain't wrong."

    "If only there’s something I can do."

    scene player_house_night with fade
    "Silas walked me to my house, gave me a soft nod, and then turned to leave toward his own."
    "before I could open my door, I was once again approached from behind."

    $ SideChar = Character("???", color="#263503", what_size=talkFont)
    SideChar "You are done with your conversation I assume?"

    "I turned around to see a figure with a long coat"

    Theo "I am sorry to intrude but the name is Theo. Theo Harper Chapman, private investigator."

    Player "and how can I help you?"

    Theo "on the contrary, it is I who can help you. I have information which may seek to your interest. ms [Player]."
    
return
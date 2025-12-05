label InteractiveGTRoom:
#placeholder
    scene bg room1
    "welcome to room 3"

#actual story:
    #interaction when player visit the detective without seeing mia
    "[Player] Went to the Jewelry store where Mia and Hannah used to work."
    #if player went to gt before
    if(mapDecisionGTfirstEncounter == False):
        $ SideChar = Character("Shop owner", color="#e5ffa7", what_size=talkFont)
        SideChar "Hello! welcome to GT Jewelry. How can I assist you today?"

        SideChar "If you're looking for something specific, feel free to ask!"

        Player "right.. I was hoping to find out about a previous employee potentially by the name of Hannah?"

        SideChar "Sorry, doesn't ring a bell. I'm the store owner and we never had a Hannah working here.
        The only people that currently works here besides myself are Mia and Rudie."

        Player "Do you mind if I ask for the previous workers or potentially regulars?"

        SideChar "Oh jeez, that'll be tough. Over the years they come and go.
        Let me see, there was a Jake, Colton, Sam, and Andrea, who previously worked here."
    
        SideChar "as for regulars all I could think of is Ajani, Rita, Chapman, Krista, and Keenan."
        "[Player] didnt get any information regarding Hannah here."
        Player "Thank you for your time, I must get going now."
        SideChar "No problem, have a great day!"
        $ mapDecisionGTfirstEncounter = True
        jump map
    #if player went to gt aftrer meeting with mia
    if((MapDecision_counter == 1 and mapDecisionGTfirstEncounter == False)):
        $ SideChar = Character("Shop owner", color="#e5ffa7", what_size=talkFont)
        SideChar "Hello! welcome to GT Jewelry. How can I assist you today?"
        SideChar "If you're looking for something specific, feel free to ask!"
        Player "right.. I was hoping to find out about a previous employee potentially by the name of Hannah?"
        SideChar "Sorry, doesn't ring a bell. I'm the store owner and we never had a Hannah working here.
        The only people that currently works here besides myself are Mia and Rudie."
        Player "Do you mind if I ask for the previous workers or potentially regulars?"
        SideChar "Oh jeez, that'll be tough. Over the years they come and go.
        Let me see, there was a Jake, Colton, Sam, and Andrea, who previously worked here."
        SideChar "as for regulars all I could think of is Ajani, Rita, Chapman, Krista, and Keenan."
        "[Player] didnt get any information regarding Hannah here."
        Player "Thank you for your time, I must get going now."
        SideChar "No problem, have a great day!"
        #if previously talked to mia
        "Mia suddenly appears at the entrance of the store."
        Mia "[Player] what are you doing here?"
        Player "oh um nothing... I could ask you the same thing!"
        "Mia looks at [Player] with a blank expression."
        Mia "I work here! \n Owner: she works here..."
        Player "oh right... sorry I forgot"
        "[Player] ran out without further questionings"
        $ mapDecisionGTfirstEncounter = True
        $ MapDecision_counter += 1 

    if (mapDecisionMiafirstEncounter == True and mapDecisionGTfirstEncounter == True):
        "[Player] Enters the store"
        SideChar "Oh hello again!"
        Player "yes um.."
        $ renpy.pause(2.5, hard=True)
        "[Player] looks around the store."
        "don't see Mia anywhere"
        Player "wheres mia?"
        SideChar "Oh, Mia? She stepped out for a moment. do you need her?"
        Player "oh no. I have a favor though can you relist the previous names for me?"
        SideChar "I am a busy person but sure"
        SideChar "Previous Employees: Jake, Colton, Sam, Andrea. \n 
        Regulars: Ajani, Rita, Chapman, Krista, Keenan. Jessi"
        Player "Thank you!"
    else:
        "[Player] Enters the store"
        SideChar "Oh hello again!"
        Player "yes um.."
        $ renpy.pause(2.5, hard=True)
        "I have a favor though can you relist the previous names for me?"
        SideChar "I am a busy person but sure"
        SideChar "Previous Employees: Jake, Colton, Sam, Andrea. \n 
        Regulars: Ajani, Rita, Chapman, Krista, Keenan. Jessi"
        Player "Thank you!"
    jump map
label InteractiveMiaRoom:
    #placeholder test
    #scene bg room1
    scene expression im.Scale("chapter1/inside the church/haley.png", config.screen_width, config.screen_height)


    #actual story
    #to increase the counter for the queue system
    if(MapDecision_counter == 0 or MapDecision_counter == 2):
        $ MapDecision_counter += 1

    #mia action after mia -> detective -> gt shop -> mia
    if(MapDecision_counter == 1 and mapDecisionMiafirstEncounter == False):
        "[Player] visits Mia at her house."
        #knocking sounds
        Player "*Knock Knock* Hey Mia, I'm sorry to bother you, but I have an important question to ask."

        #knocking sounds
        "Maybe she isn't here? [Player] thought to herself."

        Mia "{b}*Opens the door*{/b}"
        Mia "*Gasping and out of breath*\nSo *GASP*\nSORRY\nI was in the shower, haha."
        Mia "After gaining her composure, she invites [Player] in."

        Mia "So, what brings you here, cupcake?"
        Player "..."        
        Player "I..."
        $ renpy.pause(2.5, hard=True)  #waits 2.5 seconds, hard=True prevents skipping
        "I thought about how I should approach this."
        menu:
            "Ask Mia directly about Hannah or be more subtle"
            "Be direct":
                Player "Okay, so I did some research..."
                $ renpy.pause(2.5, hard=True)
                Mia "Go on."
                Player "I found out you and Hannah used to work together?"
                Mia "You mean...at GT Jewelry?"
                Player "Yeah, I heard you two were close friends and that she used to work there."
                Mia "From all my time working there, I can say Hannah was one of a kind."
                Mia "Hannah was a customer back when I first started out at the jewelry store..."
                Mia "She did help out from time to time, but I wouldn't call her an employee here."
                "[Player] learned that Hannah helped out, but is also suspicious that Mia did not bring up the incident regarding the auction."
                Player "What kind of work did she help out with?"
                Mia "Oh, you know, just the usual stuff. Helping customers, organizing inventory, that kind of thing."
                "[Player] noticed a photo on the wall of Mia and Hannah together at a party? or a gathering?"
                Player "can you tell me more about this photo?"
                Mia "**GASP**"
                Mia "oh that was just an old photo."
                "Mia seem hesitant to talk about it. I pursue no further."
                Player "Thank you, and sorry for the sudden visit. I must get going now."
                $ mapDecisionMiafirstEncounter = True

            "indirectly discuss about Hannah":
                "[Player] scans the room for clues."
                Player "I kind of just wanted to visit."
                Player "Sorry that I caught you at a bad time."
                Mia "*{b}Hugs [Player]{/b}*\nNo such thing as a bad time."
                Player "Hey, I was wondering... can you tell me more about Hannah?"
                Mia "Hannah? I mean, sure, let's see... Back when I first started out at a jewelry store, Hannah was my first customer. She walked in, carrying confidence and a smile."
                Player "What was she buying?"
                $ Mia = Character("Mia", color="#ff00ff", what_size=whisperFont) 
                Mia "Ha... Hannah buying something... *said sarcastically*"
                $ Mia = Character("Mia", color="#ff00ff", what_size=talkFont) 
                Mia "How do I say this nicely... Hannah was a flat-out broke girlie."
                Mia "I remember she was trying to get a gift for your mother but only had 90 dollars to her name."
                Mia "Despite all that confidence, I was dumbfounded."
                Player "Pft. So what happened?"
                Mia "Well, I ended up giving her a discount on a ruby necklace. She was so thankful that, over time, she kept coming to visit and we became close."
                "[Player] and Mia continue to talk about Hannah and her past; however, Mia never brought up the incident with the auction."
                $ mapDecisionMiafirstEncounter = True


    elif(MapDecision_counter >= 1 and mapDecisionMiafirstEncounter == True):
            Mia "Hello again, [Player]! Did you forget something?\nStay safe on your way home!"

    if(MapDecision_counter ==3):
        "[Player] decided to visit Mia again."
        "Mia was found tending to her garden outside."
        Mia "Back so soon?"
        Player "I can't do this anymore. I need to know the truth about Hannah."
        Player "{b}I know about the pink pendant.{/b}"
        Player "{b}I know about the auction.{/b}"
        Player "{b}I know that she was with you.{/b}"
        # Removed Player override to preserve user-chosen name
        Mia "*grabs [Player]'s hand* Enough..."
        "Mia exchanged a knowing glance with [Player], aware that [Player] was suggesting she caused Hannah's disappearance and is looking for answers."
        Mia "I know you are looking for answers, but it's not that simple."
        Mia "There are things I can't tell you, like why Hannah was with me, but please... believe me, I am not the killer."
        Mia "I just want to find out what happened to her too.\nAnd I wish I could tell you everything, but..."
        Mia "I don't have the answers. Hannah and I split up after the auction. We sold the pendant and went our separate ways."
        Player "LIES!"
        call Mia_Flashback
        "[Player] broke down, exhausted."
        Player "I believe you...\n[Player] went home."
        Mia "*as [Player] walks away* I'm sorry. I wish I could help more."
#exit once talked to everyone
    if (MapDecision_counter == 3):
        show bg forestroom with fade
        return
    else:
        jump map



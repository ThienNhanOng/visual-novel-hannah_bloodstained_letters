label InteractiveMiaRoom:
    #placeholder test
    scene bg room1
    "welcome to room 1"


    #actual story
    #to increase the counter for the queue system
    if(MapDecision_counter == 0 or MapDecision_counter == 2):
        $ MapDecision_counter += 1

    #mia action after mia -> detective -> gt shop -> mia
    if(MapDecision_counter == 1 and mapDecisionMiafirstEncounter == False):
        "[Player] visit Mia at her house"
        #knocking sounds
        Player "*Knock Knock* hey Mia im sorry to bother you but I have an important question to ask"

        # knocking sounds
        "maybe she isnt here? [Player] thought to herself"

        Mia "{b} 'Opens the door' {/b}"
        Mia "*Gasping and out of breath* \n so *GASP* \n SORRY \n I was in the shower haha"
        Mia "After gaining her composer she invite [Player] in"

        Mia "So what brings you here cupcake?"
        Player "..."        
        Player "I..."
        $ renpy.pause(2.5, hard=True)  # waits 2.5 seconds, hard=True prevents skipping
        "I thought about how I should approach this."
        menu:
            "Ask Mia directly about her work relationship with Hannah or be discrete about it?"
            "Be direct":
                Player "Okay, so I did some research..."
                $ renpy.pause(2.5, hard=True)
                Mia "Go on?"
                Player "I found out you and Hannah used to work together?"
                Mia "You mean...at GT Jewelry?"
                Player "Yeah, I heard you two were close friends and how she used to work there."
                Mia "From all my time working there, I can say Hannah was one of a kind."
                Mia "Hannah was a customer back when I first started out at a jewelry store..."
                Mia "She did help out from time to time, but I wouldn't call her an employee here."
                "[Player] learned that Hannah helps out but is also suspicious that Mia did not bring up the incident regarding the auction."
                Player "What kind of work did she help out with?"
                Mia "Oh, you know, just the usual stuff. Helping customers, organizing inventory, that kind of thing."
                "[Player] noticed a photo on the wall of Mia and Hannah together at a party, but left without saying another word."
                Player "Thank you, and sorry for the sudden visit. I must get going now."
                $ mapDecisionMiafirstEncounter = True

            "Be indirect":
                "[Player] scans the room for clues."
                Player "I kind of just wanted to visit."
                Player "Sorry that I caught you at a bad time."
                Mia "*{b}'Hugs [Player]'{/b}\nNo such thing as a bad time."
                Player "Hey, I was wondering...can you tell me more about Hannah?"
                Mia """Hannah? I mean sure, let's see...
                Back when I first started out at a jewelry store,
                Hannah was my first customer. She walked in, carrying confidence and a smile."""
                Player "What was she buying?"
                $ Mia = Character("Mia", color="#ff00ff", what_size=whisperFont) 
                Mia "Ha...Hannah buying something... *said sarcastically*"
                $ Mia = Character("Mia", color="#ff00ff", what_size=talkFont) 
                Mia "How do I say this nicely...Hannah was a flat-out broke girlie."
                Mia "I remember she was trying to get a gift for your mother but only had 90 dollars to her name."
                Mia "Despite all that confidence, I was dumbfounded."
                Player "Pft. So what happened???"
                Mia "Well, I ended up giving her a discount on a ruby necklace. She was so thankful that over time she kept coming to visit and we became close."
                "[Player] and Mia continue to talk about Hannah and her past; however, Mia never brought up the incident with the auction."
                $ mapDecisionMiafirstEncounter = True


    elif(MapDecision_counter >= 1 and mapDecisionMiafirstEncounter == True):
            Mia "hello again [Player]! did you forget something? \n Stay safe on your way home!"

    if(MapDecision_counter ==3):
        "[Player] decided to visit Mia again."
        "Mia was found tending to her garden outside"
        Mia "back so soon?"
        Player "I can't do this anymore. I need to know the truth about Hannah."
        $ Player = Character("Player", color="#25ffed", what_size=yellFont)
        Player "{b}I know about the pink pendant.{/b}"
        Player "{b}I know about the auction{/b}"
        Player "{b}I know that she was with you{/b}"
        $ Player = Character("Player", color="#25ffed", what_size=talkFont)
        Mia "grabbed [Player]'s hand. enough..."
        "Mia exchanged a knowing glance with [Player]. \n aware that [Player] suggesting that she 
        caused Hannah's disappearance. and is looking for answers"
        Mia "I know you are looking for answers, but it's not that simple."
        Mia "there are things I cant tell you like why Hannah was with me but please... believe me I am not the killer"
        Mia "I just want to find out what happened to her too. \n and I wish I can tell you everything but"
        Mia "I dont have the answers. Hannah and I split up after the auction. we sold the pendant and went our separate ways."
        Player "LIES!"
        call Mia_Flashback
        "[Player] Broke down and exhausted."
        Player "I believe you..\n [Player] went home."
        Mia "*as [Player] walks away*, I'm sorry. I wish I can help more."
#exit once talked to everyone
    if (MapDecision_counter == 3):
        return
    else:
        jump map



label InteractiveForestRoom:
    scene bg forestroom
    "welcome to room 2"
    #return back to the map after finish dialogue

    #actual story


    #interaction when player visit the detective without seeing mia
    show detective rock 
    "[Player] Went to the backwoods to visit detective Theodor {image=mcinline}"

    
    if(MapDecision_counter != 1 and mapDecisionMiafirstEncounter == False):
        scene bg forestroom
        show theo b1 at truecenter
        Theo "Ah, [Player]! What brings you to the backwoods?"
        hide theo b1
        show theo b2 at truecenter
        "There is nothing for you here"
        # Show only her image here (replace the old placeholder)
        hide theo b2
        hide detective rock
        
        
    elif (MapDecision_counter == 1 and mapDecisionMiafirstEncounter == True):
        scene bg forestroom
        show theo b2 at truecenter
        Theo "Ah, [Player]! What brings you to the backwoods?"
        show mc at truecenter
        hide theo b2 with pixellate
        Player "I met up with Mia. like you suggested"
        # Replace plain hide/show with transitions
        hide mc with pixellate
        Theo "And how did thy meeting fare?"
        show mc at left
        with moveinleft
        Player "Regarding the case, not too much.\nHowever, I did learn that Mia definitely participated at an auction, and Hannah was somewhat involved."
        Player "As you stated."
        hide mc
        show theoexcited with pixellate
        Theo "Spended! \n SPENDED!"
        hide theoexcited with pixellate
        show mc2
        Player "But...I didn't learn anything?"
        hide mc2
        "[Theo] Walks away. as he has his back turned he quoted"
        $ Theo = Character("Theo", color="#ff9100", what_size=yellFont)
        show theo b1 at right
        Theo "Patience, my friend. Time is but the silent accomplice of truth"
        hide theo b1
        Player "Wait where are you going!"
        "By the time Player could ask anything else, Theo had already disappeared deeper into the forest"
        show mcsmiling
        Player "Time silence accomplice bla bla patience..\n {b}'Some detective so helpful  -_-{/b}"
        Player "Giggles."
        $ MapDecision_counter += 1 #should increment counter to 2 here
        $ mapDecisionDetectivefirstEncounter = True
    elif (mapDecisionDetectivefirstEncounter == True):
        "There is no one here. Lets turn back."
    jump map
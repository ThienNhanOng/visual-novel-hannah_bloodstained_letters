default raisesCounter = 3 #default is 0 just made it easier for presentation
default payout = 5
default arcadecheck = False
image bg room2 = "images/map/schoolmap/bg room2.png"

#the room

#placeholder test
label trackroom:
    show trackbg
    #"welcome to the track"
    #increase time after leaving the room

    

    if currentTime() == "Morning":
        show trackbg
        Silas "exercising before class?"

    
    elif currentTime() == "Noon" and purchased_items.get("work_permit", False):
        show trackbg
        $ SideChar = Character("Coach Paige", color="#5c3304")
        SideChar "Just in time! and welcome to work! grab a rake"
        Player "on it!"
        
        play movie "visualAnimation/raking.webm"
        "you made $[payout] for raking the leaves"
        $ Global_Money += payout
        $ raisesCounter += 1

        if raisesCounter >= 5:
            $ payout += 1
            $ raisesCounter = 0 #reset counter for next raise
            SideChar "Nice work — you've earned a raise!"
    else:
        $ SideChar = Character("Coach Mark", color="#d3661d")
        SideChar "Hey! excuse me but please get off the track field"
        SideChar "this time is reserved for cleaning"
    
    if payout >= 6 and arcadecheck == False:
        $ arcadeUnlocked = True
        $ arcadecheck = True
        "You unlocked an item in the shop!"
        "buy it to access the arcade room!"  
 
    $ timeIncrease()
    jump schoolmap

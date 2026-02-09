image bg room1 = "images/bg room1.png"

# restriction boolean variables
default purchased_items = {} #dictionary to track purchased items
default fakeidUnlocked = False #through courtroom night event
default workpermitUnlocked = True #default for purchase
default hiddenletterUnlocked = False #available once all 3 condition are true
default arcadeUnlocked = False #when player get a raise to 7 dollars start at 5
default fri_noon_questions_asked = []


init python:
    # items for dictionary
    shopItems = [
        {"name": "fake_id",     "label": "Fake ID",      "price": 1,  "desc": "Access to the casino",   "condition": "fakeid_unlocked"}, #100
        {"name": "work_permit", "label": "Work Permit",  "price": 1,   "desc": "Allow you to work at school", "condition": "workpermit_unlocked"}, #30
        {"name": "letter",      "label": "Letter",       "price": 1, "desc": "???",                     "condition": "quest_completed"}, #200
        {"name": "arcade_pass", "label": "Arcade Pass",  "price": 1, "desc": "Access to the arcade",    "condition": "arcade_unlocked"}, #50
    ]

init python:
    #return item as already own, locked, too expensive or buy
    def purchaseableItem(item):
        # already owned check
        if purchased_items.get(item["name"], False):
            return False, "already owned"

        #check dictionary and if it meets the flag for "condition".
        cond = item["condition"]

        if cond == "fakeid_unlocked" and fakeidUnlocked == False:
            return False, "locked"
        if cond == "workpermit_unlocked" and workpermitUnlocked == False:
            return False, "locked"
        if cond == "quest_completed" and hiddenletterUnlocked == False:
            return False, "locked"
        if cond == "arcade_unlocked" and arcadeUnlocked == False:
            return False, "locked"

        #check if player has enough money
        if Global_Money < item["price"]:
            return False, "too expensive"
        return True, "buy"

    

    def buy_item(item):
        global Global_Money 
        #check if item can be purchased if not replace string.
        can, reason = purchaseableItem(item) #line 22 return as already own if purchase
        #pop up notification using renpy library
        if can == False:
            if reason == "already owned":
                renpy.notify("You already bought this!")
            #pop up if flag is not met
            elif reason == "locked":
                renpy.notify("Not available yet!")
            else:
            # pop up if not enough money
                renpy.notify("Not enough money!")
            return

        #if all conditions are met, complete purchase
        Global_Money -= item["price"]
        #set the purchased items true when bought
        purchased_items[item["name"]] = True
        renpy.notify("Bought {} for ${}!".format(item["label"], item["price"]))
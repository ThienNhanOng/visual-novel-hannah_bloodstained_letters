image bg room1 = "images/bg room1.png"

# restriction boolean variables
default purchased_items = {}
default questCompleted = True
default arcadeUnlocked = True
default fakeidUnlocked = True
default workpermitUnlocked = True

init python:
    # items for dictionary
    shopItems = [
        {"name": "fake_id",     "label": "Fake ID",      "price": 250,  "desc": "Access to the casino",   "condition": "fakeid_unlocked"},
        {"name": "work_permit", "label": "Work Permit",  "price": 30,   "desc": "Allow you to work at school", "condition": "workpermit_unlocked"},
        {"name": "letter",      "label": "Letter",       "price": 1000, "desc": "???",                     "condition": "quest_completed"},
        {"name": "arcade_pass", "label": "Arcade Pass",  "price": 1000, "desc": "Access to the arcade",    "condition": "arcade_unlocked"},
    ]

init python:
    def purchaseableItem(item):
        # already owned?
        if purchased_items.get(item["name"], False):
            return False, "already owned"

        # super simple condition check (baby style)
        cond = item["condition"]

        if cond == "fakeid_unlocked" and not fakeidUnlocked:
            return False, "locked"
        if cond == "workpermit_unlocked" and not workpermitUnlocked:
            return False, "locked"
        if cond == "quest_completed" and not questCompleted:
            return False, "locked"
        if cond == "arcade_unlocked" and not arcadeUnlocked:
            return False, "locked"

        # not enough money?
        if Global_Money < item["price"]:
            return False, "too expensive"

        # ok!
        return True, "can buy"


    def buy_item(item):
        global Global_Money
        can, reason = purchaseableItem(item)

        if not can:
            if reason == "already owned":
                renpy.notify("You already bought this!")
            elif reason == "locked":
                renpy.notify("Not available yet!")
            else:
                renpy.notify("Not enough money!")
            return

        # Success
        Global_Money -= item["price"]
        purchased_items[item["name"]] = True
        renpy.notify("Bought {} for ${}!".format(item["label"], item["price"]))
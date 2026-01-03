image bg room1 = "images/bg room1.png"

#restriction variables
default purchased_items = {}
default quest_completed = False
default arcade_unlocked = False
default fakeid_unlocked = True
default workpermit_unlocked = True



#Shop setup
init python:
    from enum import Enum

    #item list
    class ShopItem(Enum):
        ITEM1 = ("Fake ID", 50, "Access to the casino")
        ITEM2 = ("Work Permit", 18, "Allow you to work at school")
        ITEM3 = ("Letter", 1000, "???")
        ITEM4 = ("Arcade Pass", 1000, "Access to the arcade")
        #ITEM5 = ("Lotto ticket", 1000, "Access to the arcade")

        def __init__(self, label, price, desc):
            self.label = label
            self.price = price
            self.desc = desc


    #item conditions for each items
    def fakeidCondition():
        return fakeid_unlocked

    def workPermitCondition():
        return workpermit_unlocked

    def letterCondition():
        return quest_completed

    def arcadePassCondition():
        return arcade_unlocked


    
    # Condition Table
    ITEM_CONDITIONS = {
        ShopItem.ITEM1: fakeidCondition, #for casino
        ShopItem.ITEM2: workPermitCondition,
        ShopItem.ITEM3: letterCondition,
        ShopItem.ITEM4: arcadePassCondition,
    }


    def checkconditions(item):
        """Check if the item’s special condition is met."""
        if item in ITEM_CONDITIONS:
            return ITEM_CONDITIONS[item]()
        return True


    #Purchase system config
    def canbuy(item):
        # Only check ownership and conditions, not money
        # Money check happens in buyitem() with notification
        not_owned = not purchased_items.get(item.name, False)
        allowed = checkconditions(item)

        return not_owned and allowed


    def buyitem(item):
        global Global_Money, purchased_items

        # Check if already owned
        if purchased_items.get(item.name, False):
            renpy.notify("You already own %s." % item.label)
            return

        # Check if condition is met
        if not checkconditions(item):
            renpy.notify("You cannot purchase %s yet." % item.label)
            return

        # Check if can afford
        if Global_Money < item.price:
            renpy.notify("You don't have enough money! Need %d." % item.price)
            return

        # Purchase successful
        Global_Money -= item.price
        purchased_items[item.name] = True
        renpy.notify("Bought %s for $ %d." % (item.label, item.price))


label shopconfig:
    scene bg room1
    return
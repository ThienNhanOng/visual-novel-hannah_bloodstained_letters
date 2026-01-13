default dayIndex = 0     #0=Mon, 1=Wed, 2=Fri, 3=Weekend
default timeIndex = 0    #0=Morning, 1=Noon, 2=Night

init python:
    days = ("Mon", "Fri", "Sun")
    TimeOfDay = ("Morning", "Noon", "Night", "Bedtime")


    def timeIncrease():
        store.timeIndex += 1
        if store.timeIndex >= len(TimeOfDay):
            store.timeIndex = len(TimeOfDay) - 1  #cap at Night

    def advancedNextDay():
        """Reset day
        """
        if store.timeIndex >= 2:  #2 = Night, 3 = Bedtime
            store.dayIndex = (store.dayIndex + 1) % len(days)
            store.timeIndex = 0

    #return the current day stored in Renpy
    def currentDayLabel():
        return days[store.dayIndex]
    #return the current time of day stored in Renpy
    def currentTime():
        return TimeOfDay[store.timeIndex]
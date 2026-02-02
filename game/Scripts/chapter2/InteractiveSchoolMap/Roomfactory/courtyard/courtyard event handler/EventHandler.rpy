label eventQueue:

    $ current_day = currentDayLabel()

    #pick events from monday or friday
    if current_day == "Mon":
        $ current_events = mondayEvents
    elif current_day == "Fri":
        $ current_events = fridayEvents

    #Build the queue for the current day/time
    $ EventQueue.build(current_events)

    #Run events in the queue
    python:
        eventsFinish = False
        while True:
            event = EventQueue.pop()
            if not event:
                break
            eventsFinish = True
            renpy.call(event["name"])

    #Only show fallback if no events ran
    if not eventsFinish:
        #check if all flags are met to unlock the letter ending
        if fakeidUnlocked and workpermitUnlocked and arcadeUnlocked and not hiddenletterUnlocked:
            $ hiddenletterUnlocked = True
            "Nothing special is happening right now."
        elif currentTime() == "Morning":
            "The courtyard is bustling with students preparing for classes."
        elif currentTime() == "Noon":
            "The courtyard is empty. everyone must be in class."
        elif currentTime() == "Night":
            "The courtyard is quiet at night. Only a few students linger."
    return
init python:
    #Initialize event tracking variables
    if 'events_done' not in globals():
        events_done = set()
    
    if 'event_queue' not in globals():
        event_queue = []

    class EventQueue:

        @staticmethod
        def build(events):
            queue = []
            current_day = currentDay_label()
            current_time = currentTime()

            for event in events:
                #Skip completed events
                if event["name"] in events_done:
                    continue

                #Check if the event belongs to today
                if current_day == "Mon":
                    if not event["name"].startswith("mon"):
                        continue
                elif current_day == "Fri":
                    if not event["name"].startswith("fri"):
                        continue
                else: #in case if i need to add sunday events
                    continue

                #Check time matches
                if event["time"] != current_time:
                    continue

                queue.append(event)

            #Sort by priority (highest first)
            for i in range(len(queue)):
                for j in range(i + 1, len(queue)):
                    if queue[j]["priority"] > queue[i]["priority"]:
                        queue[i], queue[j] = queue[j], queue[i]

            store.event_queue = queue

        @staticmethod
        def pop():
            if store.event_queue:
                return store.event_queue.pop(0)
            return None

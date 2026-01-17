# Event queue variables - persistent across saves
default events_done = set()

#note the empty event queue list is defined in script
init python:

    class EventQueue:

        @staticmethod
        def build(events):
            queue = []
            current_day = currentDayLabel()
            current_time = currentTime()

            for event in events:
                #Skip completed events
                if event["name"] in events_done:
                    continue

                #Check if the event belongs to today
                if current_day == "Mon":
                    if event["name"].startswith("mon") == False:
                        continue
                elif current_day == "Fri":
                    if event["name"].startswith("fri") == False:
                        continue
                else: #In case if i need to add sunday events
                    continue

                #Check time matches
                if event["time"] != current_time:
                    continue

                queue.append(event)

            #bubble sort for priority (highest first)
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

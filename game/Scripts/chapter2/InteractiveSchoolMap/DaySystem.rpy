default day_index = 0     # 0=Mon, 1=Wed, 2=Fri, 3=Weekend
default time_index = 0    # 0=Morning, 1=Noon, 2=Night

init python:
    days = ("Mon", "Fri", "Sun")
    TimeOfDay = ("Morning", "Noon", "Night", "Bedtime")


    def timeIncrease():
        store.time_index += 1
        if store.time_index >= len(TimeOfDay):
            store.time_index = len(TimeOfDay) - 1  # cap at Night

    def advance_day_if_night():
        """
        If the current time is Night or Bedtime, advance to the next day
        and reset time to Morning.
        """
        if store.time_index >= 2:  # 2 = Night, 3 = Bedtime
            store.day_index = (store.day_index + 1) % len(days)
            store.time_index = 0

    def current_day_label():
        return days[store.day_index]

    def currentTime():
        return TimeOfDay[store.time_index]

    def current_time_label():
        # Kept for convenience; combines day and time of day.
        return f"{current_day_label()}  {currentTime()}"
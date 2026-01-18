#Friday Events - Individual labels for each event

#===== FRIDAY MORNING EVENTS =====

label fri_morning_morningCheckIn:
    $ SideChar = Character("Guidance Officer", color="#2c3e50")
    SideChar "Morning, [Player]. Quick check-in: feeling ready for the day?"
    menu:
        "I'm prepared":
            SideChar "Love the energy. Keep that focus in class."
        "Not really":
            SideChar "Take a breath. You can still turn it around today."
    $ events_done.add("fri_morning_morningCheckIn")
    return

label fri_morning_foundNotebook:
    $ SideChar = Character("Student Volunteer", color="#16a085")
    SideChar "Did you drop this notebook?"
    menu:
        "Yes, that's mine":
            SideChar "Here you go. Maybe add a name tag next time."
        "No, but I'll turn it in":
            SideChar "Thanks. Lost and found is by the admin office."
    $ events_done.add("fri_morning_foundNotebook")
    return

label fri_morning_coachStretch:
    $ SideChar = Character("Coach Lee", color="#d35400")
    SideChar "Light stretches to wake up your muscles. Join in?"
    menu:
        "I'm in":
            SideChar "Arms up, deep breath... that's it."
        "Maybe later":
            SideChar "Alright, just don't sit all day."
    $ events_done.add("fri_morning_coachStretch")
    return

#===== FRIDAY NOON EVENTS =====

label fri_noon_jeopardy:
    $ Host = Character("Quiz Host", color="#c0392b")
    $ questions = [
        ("What is the capital of France?", "paris", 12),
        ("Chemical symbol for sodium?", "na", 10),
        ("Who painted the Mona Lisa?", "da vinci", 15),
        ("Solve: 9 multiplied by 7", "63", 9),
        ("Author of '1984'?", "george orwell", 11),
    ]
    $ available_questions = [q for q in questions if q[0] not in fri_noon_questions_asked]
    if len(available_questions) == 0:
        $ fri_noon_questions_asked = []
        $ available_questions = questions
    $ prompt, correct_answer, reward = renpy.random.choice(available_questions)
    $ fri_noon_questions_asked.append(prompt)
    Host "Welcome to Courtyard Jeopardy! Answer correctly for a quick prize."
    $ user_answer = renpy.input(prompt + " (type your answer)").strip().lower()
    if user_answer == correct_answer:
        Host "Correct! Nice reflexes."
        $ Global_Money += reward
        "You earned $[reward]."
    else:
        Host "Close, but the right answer is [correct_answer]."
    $ events_done.add("fri_noon_jeopardy")
    return

label fri_noon_groupNotes:
    $ SideChar = Character("Study Buddy", color="#2980b9")
    SideChar "Sharing notes before the quiz. Want to trade?"
    menu:
        "Trade notes":
            SideChar "Thanks. Your handwriting is way cleaner."
        "I'll stick with mine":
            SideChar "No worries. Hope yours are solid!"
    $ events_done.add("fri_noon_groupNotes")
    return

label fri_noon_snackCart:
    $ SideChar = Character("Snack Vendor", color="#8e44ad")
    SideChar "Friday discount! Fresh sandwiches for $8."
    menu:
        "I'll take one":
            SideChar "Here you go. Fuel up!"
            $ Global_Money -= 8
            "You lost $8."
        "Maybe later":
            SideChar "Deal lasts till the cart runs out."
    $ events_done.add("fri_noon_snackCart")
    return

#===== FRIDAY NIGHT EVENTS =====

label fri_night_clubCleanup:
    $ SideChar = Character("Club President", color="#7f8c8d")
    SideChar "We need an extra pair of hands to pack up. Helps keep the courtyard tidy."
    menu:
        "I'll help":
            SideChar "Appreciate it. Here's a small stipend."
            $ Global_Money += 12
            "You earned $12."
        "Can't tonight":
            SideChar "Alright, we'll manage."
    $ events_done.add("fri_night_clubCleanup")
    return

label fri_night_silasWrapup:
    Silas "Long week, huh? How are you holding up?"
    menu:
        "Doing alright":
            Silas "Good. Let's keep that momentum."
            $ Silas_counter += 1
        "Exhausted":
            Silas "Rest this weekend. I'll text if something comes up."
    $ events_done.add("fri_night_silasWrapup")
    return

label fri_night_meditation:
    $ SideChar = Character("Wellness Leader", color="#27ae60")
    SideChar "Join a 5-minute breathing session?"
    menu:
        "Yes, I need it":
            SideChar "Inhale... exhale... let the week go."
        "I'll pass":
            SideChar "All good. Find rest in your own way."
    $ events_done.add("fri_night_meditation")
    return

label fri_night_weekendReflection:
    "The courtyard quiets down; only a few lights remain as the campus settles for the weekend."
    "{Player} reflects on the how school has been the joy that it brought."
    "however she still think of the incident."
    menu:
        "Search for Hannah one last time?":
            jump investigating_the_school
        "I should just go home and rest. I have already moved on":
            pass
    $ events_done.add("fri_night_weekendReflection")
    return

#Monday Events - Individual labels for each event

label mon_morning_breakfastWithSilas:
    Silas "Hey [Player], care to join me for breakfast before class?"
    menu:
        "Sure, sounds good!":
            Silas "Great! I found this quiet spot in the courtyard."
            "You and Silas enjoy a peaceful breakfast together."
            $ Silas_counter += 1
        "Maybe next time.":
            Silas "No worries, catch you later then."
    $ events_done.add("mon_morning_breakfastWithSilas")
    return

label mon_morning_professorLecture:
    $ SideChar = Character("Professor Mills", color="#5c3304")
    SideChar "Good morning! Don't forget we have a special lecture today at 9 AM sharp."
    Player "Thank you for the reminder, Professor."
    SideChar "You're welcome. See you in class!"
    $ events_done.add("mon_morning_professorLecture")
    return

label mon_morning_clubAdvertiser:
    $ SideChar = Character("Club Member", color="#ff6b9d")
    SideChar "Excuse me! Are you interested in joining the Literature Club?"
    menu:
        "Tell me more about it.":
            SideChar "We meet every Wednesday to discuss books and creative writing!"
            Player "That sounds interesting. I'll think about it."
        "Not right now, thanks.":
            SideChar "No problem! If you change your mind, we're always welcoming new members."
    $ events_done.add("mon_morning_clubAdvertiser")
    return

label mon_morning_sageEncounter:
    Sage "Morning! You're here early too?"
    Player "Yeah, thought I'd get some fresh air before class starts."
    Sage "Same here. The courtyard is peaceful at this hour."
    "You both enjoy the quiet morning atmosphere together."
    $ events_done.add("mon_morning_sageEncounter")
    return

label mon_morning_lostStudent:
    $ SideChar = Character("Lost Freshman", color="#ffd700")
    SideChar "Um, excuse me... do you know where the main lecture hall is?"
    menu:
        "Point them in the right direction":
            Player "Sure! Go straight through that door and take a left."
            SideChar "Thank you so much! I was getting really worried."
        "Sorry, I'm new here too":
            SideChar "Oh, okay... I'll keep looking then."
    $ events_done.add("mon_morning_lostStudent")
    return

#===== MONDAY NOON EVENTS =====

label mon_noon_mathLecture:
    $ SideChar = Character("Professor Carter", color="#4a90e2")
    SideChar "Ah, perfect timing! I need a volunteer for a quick math problem."
    SideChar "What is the derivative of x²?"
    menu:
        "2x":
            SideChar "Excellent! You've been paying attention in class."
            $ Global_Money += 10
            "You earned $10."
        "x²":
            SideChar "Not quite. Review your calculus notes."
        "I don't know":
            SideChar "That's okay. Come to office hours if you need help."
    $ events_done.add("mon_noon_mathLecture")
    return

label mon_noon_lunchWithSilas:
    Silas "Hey! Want to grab lunch together?"
    menu:
        "Sure, I'm starving!":
            Silas "Great! I know a good spot."
            "You share a meal and talk about classes."
            $ Silas_counter += 1
            $ Global_Money -= 10
            "You lost $10."
        "Already ate, sorry":
            Silas "No worries, maybe next time!"
    $ events_done.add("mon_noon_lunchWithSilas")
    return

label mon_noon_englishQuiz:
    $ SideChar = Character("Professor Hayes", color="#8b4513")
    SideChar "Quick pop quiz! Who wrote 'Romeo and Juliet'?"
    menu:
        "William Shakespeare":
            SideChar "Perfect! You know your classics."
            $ Global_Money += 12
            "You earned $12."
        "Charles Dickens":
            SideChar "Not quite. Shakespeare is the answer."
        "I'm not sure":
            SideChar "It's Shakespeare. Make sure to read the assigned materials!"
    $ events_done.add("mon_noon_englishQuiz")
    return

label mon_noon_studyGroup:
    $ SideChar = Character("Study Leader", color="#9b59b6")
    SideChar "We're forming a study group for the upcoming exams. Interested?"
    menu:
        "Count me in!":
            SideChar "Awesome! We meet every Tuesday and Thursday."
        "I prefer studying alone":
            SideChar "Fair enough. Good luck with your studies!"
    $ events_done.add("mon_noon_studyGroup")
    return

label mon_noon_artClubDemo:
    $ SideChar = Character("Art Student", color="#e74c3c")
    SideChar "We're doing a live painting demonstration! Want to try?"
    menu:
        "I'd love to!":
            SideChar "Great! Here's a brush and canvas."
            "You spend some time painting and relaxing."
            $ Global_Money -= 6
            "You lost $6."
        "Just watching is fine":
            SideChar "No problem! Enjoy the show!"
    $ events_done.add("mon_noon_artClubDemo")
    return

label mon_noon_libraryTip:
    $ SideChar = Character("Librarian", color="#16a085")
    SideChar "Did you know we have extended hours during exam week?"
    Player "Oh really? That's helpful to know!"
    SideChar "Yes! We're open until midnight. Take advantage of it!"
    $ events_done.add("mon_noon_libraryTip")
    return

label mon_noon_sportsPractice:
    $ SideChar = Character("Coach Williams", color="#f39c12")
    SideChar "We need one more player for basketball practice. You in?"
    menu:
        "Sure, I'll join!":
            SideChar "Excellent! Let's see what you've got."
            "You play basketball for a while."
        "Not today":
            SideChar "Alright, maybe another time!"
    $ events_done.add("mon_noon_sportsPractice")
    return

label mon_noon_scienceLab:
    $ SideChar = Character("Dr. Martinez", color="#27ae60")
    SideChar "Quick chemistry question! What's the chemical symbol for gold?"
    menu:
        "Au":
            SideChar "Correct! You know your periodic table!"
            $ Global_Money += 12
            "You earned $12."
        "Go":
            SideChar "Close, but it's Au from the Latin 'Aurum'."
        "I don't remember":
            SideChar "It's Au. Chemistry requires memorization!"
    $ events_done.add("mon_noon_scienceLab")
    return

label mon_noon_musicPerformance:
    $ SideChar = Character("Music Student", color="#e67e22")
    SideChar "I'm practicing for my recital. Mind listening and giving feedback?"
    menu:
        "I'd be happy to!":
            SideChar "Thank you! Here goes..."
            "You listen to a beautiful piano performance."
        "Sorry, I'm in a hurry":
            SideChar "That's okay, thanks anyway!"
    $ events_done.add("mon_noon_musicPerformance")
    return

label mon_noon_friendlyChat:
    $ SideChar = Character("Friendly Student", color="#3498db")
    SideChar "Hey! You're in my history class, right?"
    Player "Yeah, I think so!"
    SideChar "Cool! Want to exchange notes sometime?"
    menu:
        "Sure, that'd be great!":
            SideChar "Awesome! Here's my number."
        "Maybe later":
            SideChar "No problem, just let me know!"
    $ events_done.add("mon_noon_friendlyChat")
    return

#===== MONDAY NIGHT EVENTS =====

label mon_night_nightStudy:
    $ SideChar = Character("Night Tutor", color="#9b59b6")
    SideChar "Evening study sessions are great for retention. Need help with anything?"
    menu:
        "Yes, I'm struggling with physics":
            SideChar "Let me explain momentum. It's mass times velocity."
        "I'm good, thanks":
            SideChar "Alright, good luck with your studies!"
    $ events_done.add("mon_night_nightStudy")
    return

label mon_night_silasStargazing:
    Silas "The stars are beautiful tonight. Want to stargaze for a bit?"
    menu:
        "That sounds peaceful":
            Silas "Look, that's the Big Dipper!"
            "You spend time stargazing together."
            $ Silas_counter += 2
        "I should head back":
            Silas "Understandable. Don't stay out too late!"
    $ events_done.add("mon_night_silasStargazing")
    return

label mon_night_historyQuestion:
    $ SideChar = Character("Night Professor", color="#8b4513")
    SideChar "Still awake? Good! When did World War II end?"
    menu:
        "1945":
            SideChar "Correct! September 2nd, 1945 to be exact."
            $ Global_Money += 12
            "You earned $12."
        "1944":
            SideChar "Close, but it ended in 1945."
        "I'm not sure":
            SideChar "It's 1945. Important date to remember!"
    $ events_done.add("mon_night_historyQuestion")
    return

label mon_night_lateLibrary:
    $ SideChar = Character("Night Librarian", color="#16a085")
    SideChar "The library closes in 30 minutes. Need to borrow anything?"
    menu:
        "I need a textbook":
            SideChar "Here you go. Return it by Friday!"
            "You borrow a useful textbook."
        "I'm just browsing":
            SideChar "Take your time, but remember the closing time."
    $ events_done.add("mon_night_lateLibrary")
    return

label mon_night_nightShift:
    $ SideChar = Character("Manager", color="#f39c12")
    SideChar "We need someone for a quick night shift stocking shelves. Pays well!"
    menu:
        "I'll take it!":
            SideChar "Great! It's just two hours of work."
            "You work for two hours."
            $ Global_Money += 15
            "You earned $15."
        "Too tired tonight":
            SideChar "Understood. Have a good night!"
    $ events_done.add("mon_night_nightShift")
    return

label mon_night_astronomyClub:
    $ SideChar = Character("Astronomy Student", color="#34495e")
    SideChar "We're using the telescope tonight. Want to see Jupiter?"
    menu:
        "That sounds amazing!":
            SideChar "Look through here! You can see the bands!"
            "You view Jupiter through the telescope."
        "Maybe another time":
            SideChar "No worries, we do this every Monday!"
    $ events_done.add("mon_night_astronomyClub")
    return

label mon_night_nightGuard:
    $ SideChar = Character("Security Guard", color="#7f8c8d")
    SideChar "You're out late. Everything okay?"
    Player "Just finishing up some studying."
    SideChar "Alright, but don't stay too late. Campus can be eerie at night."
    SideChar "you should live a bit maybe hit up the casino. dont tell anyone i said that though"
    Player "I dont know i dont want to ruin my chances of graduating"
    SideChar "pft overrated ill tell you a secret"
    SideChar "go to the bookstore and say the code 'no games no life'"
    SideChar "theyll hand you a fake id"
    "in the morning I went to the bookstore and said the code 'no games no life'"
    $ fakeidUnlocked = True
    $ events_done.add("mon_night_nightGuard")
    return

label mon_noon_arcade:
    Silas "You're out late. Everything okay?"
    Player "Just finishing up some studying."
    Player "I am behind in my work and need a break"
    Silas "why not check out the arcade? I heard they have a new racing game"
    "silas handed me a card"
    "School arcade is for hard working students!"
    Silas "try to get a raise at your track job maybe they will let you buy an access pass"
    Player "thanks for the motivation silas"
    return

label mon_night_philosophyDebate:
    $ SideChar = Character("Philosophy Student", color="#9b59b6")
    SideChar "If a tree falls in a forest and no one's around, does it make a sound?"
    menu:
        "Yes, sound waves exist regardless":
            SideChar "Interesting perspective! Physics-based reasoning."
        "No, sound requires perception":
            SideChar "Ah, a philosophical approach! I like it."
        "Let's not get into this":
            SideChar "Fair enough, it's late anyway!"
    $ events_done.add("mon_night_philosophyDebate")
    return

label mon_night_midnightSnack:
    $ SideChar = Character("Late Night Vendor", color="#e74c3c")
    SideChar "Late night snacks! Hot dogs, chips, drinks!"
    menu:
        "I'll take a hot dog":
            SideChar "Here you go! That'll be $5."
            "You enjoy a late night snack."
            $ Global_Money -= 5
            "You lost $5."
        "Just window shopping":
            SideChar "Come back if you get hungry!"
    $ events_done.add("mon_night_midnightSnack")
    return

label mon_night_mysteryShadow:
    "You notice a strange shadow moving across the courtyard."
    "It disappears before you can get a closer look."
    Player "What was that...?"
    "The night feels a bit more mysterious now."
    $ events_done.add("mon_night_mysteryShadow")
    return

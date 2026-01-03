#creating the room
#
init -90 python:
    # define the courtyard room using factory pattern
    class CourtyardRoom(Room):
        def __init__(self):
            super().__init__(
                room_id="Courtyard",
                name="Courtyard",
                idle="images/map/schoolmap/courtyard/idle_courtyard.png",
                hover="images/map/schoolmap/courtyard/hover_courtyard.png",
                xpos=890,
                ypos=700,
                label_name="courtyardroom"
            )

            #use command pattern to call the room
            self.command = CallRoom(self.label_name)

        def enter(self):
            renpy.call_in_new_context(self.label_name)

    addroom(CourtyardRoom())


label courtyardroom:
    scene bg room1
    
    # Check current day and time
    $ current_day = current_day_label()
    $ current_time = currentTime()


    # ===== MONDAY =====
    if current_day == "Mon":
        if current_time == "Morning":
            # ===== MONDAY MORNING =====
            
            #define events for Monday Morning
            default event1_breakfastWithSilas = False
            default event2_professorLecture = False
            default event3_clubAdvertiser = False
            default event4_sageEncounter = False
            default event5_lostStudent = False
            
            # Event 1: Breakfast with Silas
            if not event1_breakfastWithSilas:
                Silas "Hey [Player], care to join me for breakfast before class?"
                menu:
                    "Sure, sounds good!":
                        Silas "Great! I found this quiet spot in the courtyard."
                        "You and Silas enjoy a peaceful breakfast together."
                        $ Silas_counter += 1
                    "Maybe next time.":
                        Silas "No worries, catch you later then."
                $ event1_breakfastWithSilas = True
            
            # Event 2: Professor's Early Lecture Reminder
            elif not event2_professorLecture:
                $ SideChar = Character("Professor Mills", color="#5c3304")
                SideChar "Good morning! Don't forget we have a special lecture today at 9 AM sharp."
                Player "Thank you for the reminder, Professor."
                SideChar "You're welcome. See you in class!"
                $ event2_professorLecture = True
            
            # Event 3: Club Advertiser
            elif not event3_clubAdvertiser:
                $ SideChar = Character("Club Member", color="#ff6b9d")
                SideChar "Excuse me! Are you interested in joining the Literature Club?"
                menu:
                    "Tell me more about it.":
                        SideChar "We meet every Wednesday to discuss books and creative writing!"
                        Player "That sounds interesting. I'll think about it."
                    "Not right now, thanks.":
                        SideChar "No problem! If you change your mind, we're always welcoming new members."
                $ event3_clubAdvertiser = True
            
            # Event 4: Sage Encounter
            elif not event4_sageEncounter:
                Sage "Morning! You're here early too?"
                Player "Yeah, thought I'd get some fresh air before class starts."
                Sage "Same here. The courtyard is peaceful at this hour."
                "You both enjoy the quiet morning atmosphere together."
                $ event4_sageEncounter = True
            
            # Event 5: Lost Student
            elif not event5_lostStudent:
                $ SideChar = Character("Lost Freshman", color="#ffd700")
                SideChar "Um, excuse me... do you know where the main lecture hall is?"
                menu:
                    "Point them in the right direction":
                        Player "Sure! Go straight through that door and take a left."
                        SideChar "Thank you so much! I was getting really worried."
                        
                    "Sorry, I'm new here too":
                        SideChar "Oh, okay... I'll keep looking then."
                $ event5_lostStudent = True
            
            else:
                # Default Monday morning interaction
                "The courtyard is bustling with students preparing for Monday classes."
                "You take a moment to enjoy the morning atmosphere."
        elif current_time == "Noon":
            # ===== MONDAY NOON =====
            
            #define events for Monday Noon
            default event1_mathLecture = False
            default event2_lunchWithSilas = False
            default event3_englishQuiz = False
            default event4_studyGroup = False
            default event5_artClubDemo = False
            default event6_libraryTip = False
            default event7_sportsPractice = False
            default event8_scienceLab = False
            default event9_musicPerformance = False
            default event10_friendlyChat = False
            
            # Event 1: Math Lecture Question
            if not event1_mathLecture:
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
                $ event1_mathLecture = False
            
            # Event 2: Lunch with Silas
            elif not event2_lunchWithSilas:
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
                $ event2_lunchWithSilas = True
            
            # Event 3: English Literature Quiz
            elif not event3_englishQuiz:
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
                $ event3_englishQuiz = True
            
            # Event 4: Study Group Invitation
            elif not event4_studyGroup:
                $ SideChar = Character("Study Leader", color="#9b59b6")
                SideChar "We're forming a study group for the upcoming exams. Interested?"
                menu:
                    "Count me in!":
                        SideChar "Awesome! We meet every Tuesday and Thursday."
                        
                    "I prefer studying alone":
                        SideChar "Fair enough. Good luck with your studies!"
                $ event4_studyGroup = True
            
            # Event 5: Art Club Demo
            elif not event5_artClubDemo:
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
                $ event5_artClubDemo = True
            
            # Event 6: Library Tip
            elif not event6_libraryTip:
                $ SideChar = Character("Librarian", color="#16a085")
                SideChar "Did you know we have extended hours during exam week?"
                Player "Oh really? That's helpful to know!"
                SideChar "Yes! We're open until midnight. Take advantage of it!"
                $ event6_libraryTip = True
            
            # Event 7: Sports Practice
            elif not event7_sportsPractice:
                $ SideChar = Character("Coach Williams", color="#f39c12")
                SideChar "We need one more player for basketball practice. You in?"
                menu:
                    "Sure, I'll join!":
                        SideChar "Excellent! Let's see what you've got."
                        "You play basketball for a while."
                        
                    "Not today":
                        SideChar "Alright, maybe another time!"
                $ event7_sportsPractice = True
            
            # Event 8: Science Lab Challenge
            elif not event8_scienceLab:
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
                $ event8_scienceLab = True
            
            # Event 9: Music Performance
            elif not event9_musicPerformance:
                $ SideChar = Character("Music Student", color="#e67e22")
                SideChar "I'm practicing for my recital. Mind listening and giving feedback?"
                menu:
                    "I'd be happy to!":
                        SideChar "Thank you! Here goes..."
                        "You listen to a beautiful piano performance."
                        
                    "Sorry, I'm in a hurry":
                        SideChar "That's okay, thanks anyway!"
                $ event9_musicPerformance = True
            
            # Event 10: Friendly Chat with Random Student
            elif not event10_friendlyChat:
                $ SideChar = Character("Friendly Student", color="#3498db")
                SideChar "Hey! You're in my history class, right?"
                Player "Yeah, I think so!"
                SideChar "Cool! Want to exchange notes sometime?"
                menu:
                    "Sure, that'd be great!":
                        SideChar "Awesome! Here's my number."
                        
                    "Maybe later":
                        SideChar "No problem, just let me know!"
                $ event10_friendlyChat = True
            
            else:
                # Default Monday noon interaction
                "The courtyard is filled with students enjoying their lunch break."
                "You find a quiet spot to relax."
        
        elif current_time == "Night":
            # ===== MONDAY NIGHT =====
            
            #define events for Monday Night
            default event1_nightStudy = False
            default event2_silasStargazing = False
            default event3_historyQuestion = False
            default event4_lateLibrary = False
            default event5_nightShift = False
            default event6_astronomyClub = False
            default event7_nightGuard = False
            default event8_philosophyDebate = False
            default event9_midnightSnack = False
            default event10_mysteryShadow = False
            
            # Event 1: Night Study Session
            if not event1_nightStudy:
                $ SideChar = Character("Night Tutor", color="#9b59b6")
                SideChar "Evening study sessions are great for retention. Need help with anything?"
                menu:
                    "Yes, I'm struggling with physics":
                        SideChar "Let me explain momentum. It's mass times velocity."
                        
                    "I'm good, thanks":
                        SideChar "Alright, good luck with your studies!"
                $ event1_nightStudy = True
            
            # Event 2: Stargazing with Silas
            elif not event2_silasStargazing:
                Silas "The stars are beautiful tonight. Want to stargaze for a bit?"
                menu:
                    "That sounds peaceful":
                        Silas "Look, that's the Big Dipper!"
                        "You spend time stargazing together."
                        $ Silas_counter += 2
                    "I should head back":
                        Silas "Understandable. Don't stay out too late!"
                $ event2_silasStargazing = True
            
            # Event 3: History Question
            elif not event3_historyQuestion:
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
                $ event3_historyQuestion = True
            
            # Event 4: Late Night Library
            elif not event4_lateLibrary:
                $ SideChar = Character("Night Librarian", color="#16a085")
                SideChar "The library closes in 30 minutes. Need to borrow anything?"
                menu:
                    "I need a textbook":
                        SideChar "Here you go. Return it by Friday!"
                        "You borrow a useful textbook."
                    "I'm just browsing":
                        SideChar "Take your time, but remember the closing time."
                $ event4_lateLibrary = True
            
            # Event 5: Night Work Shift
            elif not event5_nightShift:
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
                $ event5_nightShift = True
            
            # Event 6: Astronomy Club
            elif not event6_astronomyClub:
                $ SideChar = Character("Astronomy Student", color="#34495e")
                SideChar "We're using the telescope tonight. Want to see Jupiter?"
                menu:
                    "That sounds amazing!":
                        SideChar "Look through here! You can see the bands!"
                        "You view Jupiter through the telescope."
                        
                    "Maybe another time":
                        SideChar "No worries, we do this every Monday!"
                $ event6_astronomyClub = True
            
            # Event 7: Night Security Guard
            elif not event7_nightGuard:
                $ SideChar = Character("Security Guard", color="#7f8c8d")
                SideChar "You're out late. Everything okay?"
                Player "Just finishing up some studying."
                SideChar "Alright, but don't stay too late. Campus can be eerie at night."
                $ event7_nightGuard = True
            
            # Event 8: Philosophy Debate
            elif not event8_philosophyDebate:
                $ SideChar = Character("Philosophy Student", color="#9b59b6")
                SideChar "If a tree falls in a forest and no one's around, does it make a sound?"
                menu:
                    "Yes, sound waves exist regardless":
                        SideChar "Interesting perspective! Physics-based reasoning."
                        
                    "No, sound requires perception":
                        SideChar "Ah, a philosophical approach! I like it."
                        
                    "Let's not get into this":
                        SideChar "Fair enough, it's late anyway!"
                $ event8_philosophyDebate = True
            
            # Event 9: Midnight Snack Run
            elif not event9_midnightSnack:
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
                $ event9_midnightSnack = True
            
            # Event 10: Mystery Shadow
            elif not event10_mysteryShadow:
                "You notice a strange shadow moving across the courtyard."
                "It disappears before you can get a closer look."
                Player "What was that...?"
                "The night feels a bit more mysterious now."
                $ event10_mysteryShadow = True
            
            else:
                # Default Monday night interaction
                "The courtyard is quiet at night."
                "Only a few students remain, finishing up their evening activities."
                "You take a moment to enjoy the peaceful atmosphere."
    
    # ===== FRIDAY =====
    elif current_day == "Fri":
        if current_time == "Morning":
            # ===== FRIDAY MORNING =====
            #define events for Friday Morning
            default fri_event1_morningCheckIn = False
            default fri_event2_foundNotebook = False
            default fri_event3_coachStretch = False

            # Event 1: Campus check-in
            if not fri_event1_morningCheckIn:
                $ SideChar = Character("Guidance Officer", color="#2c3e50")
                SideChar "Morning, [Player]. Quick check-in: feeling ready for the day?"
                menu:
                    "I'm prepared":
                        SideChar "Love the energy. Keep that focus in class."
                    "Not really":
                        SideChar "Take a breath. You can still turn it around today."
                $ fri_event1_morningCheckIn = True

            # Event 2: Found notebook
            elif not fri_event2_foundNotebook:
                $ SideChar = Character("Student Volunteer", color="#16a085")
                SideChar "Did you drop this notebook?"
                menu:
                    "Yes, that's mine":
                        SideChar "Here you go. Maybe add a name tag next time."
                    "No, but I'll turn it in":
                        SideChar "Thanks. Lost and found is by the admin office."
                $ fri_event2_foundNotebook = True

            # Event 3: Coach-led stretching
            elif not fri_event3_coachStretch:
                $ SideChar = Character("Coach Lee", color="#d35400")
                SideChar "Light stretches to wake up your muscles. Join in?"
                menu:
                    "I'm in":
                        SideChar "Arms up, deep breath... that's it."
                    "Maybe later":
                        SideChar "Alright, just don't sit all day."
                $ fri_event3_coachStretch = True

            else:
                "The courtyard hums with Friday energy as everyone rushes to finish the week strong."
        elif current_time == "Noon":
            # ===== FRIDAY NOON =====
            #define events for Friday Noon
            default fri_noon_event1_jeopardy = False
            default fri_noon_questions_asked = []
            default fri_noon_event2_groupNotes = False
            default fri_noon_event3_snackCart = False

            # Event 1: Courtyard Jeopardy (randomized question + input)
            if not fri_noon_event1_jeopardy:
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
                $ fri_noon_event1_jeopardy = True

            # Event 2: Group notes swap
            elif not fri_noon_event2_groupNotes:
                $ SideChar = Character("Study Buddy", color="#2980b9")
                SideChar "Sharing notes before the quiz. Want to trade?"
                menu:
                    "Trade notes":
                        SideChar "Thanks. Your handwriting is way cleaner."
                    "I'll stick with mine":
                        SideChar "No worries. Hope yours are solid!"
                $ fri_noon_event2_groupNotes = True

            # Event 3: Snack cart deal
            elif not fri_noon_event3_snackCart:
                $ SideChar = Character("Snack Vendor", color="#8e44ad")
                SideChar "Friday discount! Fresh sandwiches for $8."
                menu:
                    "I'll take one":
                        SideChar "Here you go. Fuel up!"
                        $ Global_Money -= 8
                        "You lost $8."
                    "Maybe later":
                        SideChar "Deal lasts till the cart runs out."
                $ fri_noon_event3_snackCart = True

            else:
                "Students huddle in study circles, some celebrating early starts to the weekend."
        elif current_time == "Night":
            # ===== FRIDAY NIGHT =====
            #define events for Friday Night
            default fri_night_event1_clubCleanup = False
            default fri_night_event2_silasWrapup = False
            default fri_night_event3_meditation = False

            # Event 1: Club cleanup
            if not fri_night_event1_clubCleanup:
                $ SideChar = Character("Club President", color="#7f8c8d")
                SideChar "We need an extra pair of hands to pack up. Helps keep the courtyard tidy."
                menu:
                    "I'll help":
                        SideChar "Appreciate it. Here's a small stipend."
                        $ Global_Money += 12
                        "You earned $12."
                    "Can't tonight":
                        SideChar "Alright, we'll manage."
                $ fri_night_event1_clubCleanup = True

            # Event 2: Silas weekly wrap-up
            elif not fri_night_event2_silasWrapup:
                Silas "Long week, huh? How are you holding up?"
                menu:
                    "Doing alright":
                        Silas "Good. Let's keep that momentum."
                        $ Silas_counter += 1
                    "Exhausted":
                        Silas "Rest this weekend. I'll text if something comes up."
                $ fri_night_event2_silasWrapup = True

            # Event 3: Quiet meditation circle
            elif not fri_night_event3_meditation:
                $ SideChar = Character("Wellness Leader", color="#27ae60")
                SideChar "Join a 5-minute breathing session?"
                menu:
                    "Yes, I need it":
                        SideChar "Inhale... exhale... let the week go."
                    "I'll pass":
                        SideChar "All good. Find rest in your own way."
                $ fri_night_event3_meditation = True

            else:
                "The courtyard quiets down; only a few lights remain as the campus settles for the weekend."
    
    # ===== SUNDAY =====
    elif current_day == "Sun":
        if current_time == "Morning":
            "its sunday morning"
            "there is no school today"
            pass
        elif current_time == "Noon":
            "its sunday afternoon"
            "there is no school today"
            pass
        elif current_time == "Night":
            "its sunday night"
            "there is no school today"
            pass

    #increase time after leaving the room
    $ timeIncrease()

    jump schoolmap
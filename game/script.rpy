



#library imports

#talk font
define talkFont = 43
define whisperFont = 28
define yellFont = 65

#characters variables
define Player = Character("Player", color="#25ffed", what_size=talkFont)
define Silas = Character("Silas", color="#ff0000", what_size=talkFont)  
define Theo = Character("Theo", color="#ff9100", what_size=talkFont)  
define Sage = Character("Sage", color="#1e9453", what_size=talkFont)  
define Asher = Character("Asher", color="#ffff00", what_size=talkFont)  
define Mia = Character("Mia", color="#ff00ff", what_size=talkFont)  
define Lorenzo = Character("Geralt", color="#7b887b", what_size=talkFont)
default SideChar = Character("sideCharacter", color="#e5ffa7", what_size=talkFont)

#initiate character counters for routes
define Silas_counter = 0 #
define Theo_counter = 0 #
define Mia_counter = 0 
define Global_Money = 1 # Player's start money

#money limit to limit text overflowing
if(Global_Money >= 999):
    $ Global_Money = 999

#route decisions
#1: chapter 1 player determine player choose investigate or move on
default StoryDecision_Chapter1_Investigate = False #false = peaceful route
default StoryDecision_Chapter1_Schoolname = "school"
default chapter2continue = False #flag to continue chapter 2 after peaceful reroute.
#start of game
label start:


#testing
    
    call screen schoolmapScreen

#testing end

    stop music fadeout 2.0
    #ch 0 / no location
    #summary: set up the Player prior to starting game. 
    #Player input name here.

    scene black  # Setting the background to black (or replace with your desired background image)
    
    "Welcome to the story of Hannah. The Bloodstained Letters."
    "Little girl, What is your name?"
    
    $ name = renpy.input("Enter your name:").strip() or "Leah"  # Default name if input is empty
    $ name = name.capitalize()  # Capitalize the first letter of the name
    "Ah! I remember now, your name is [name]! Anyhow, let's get started!"
    
    #override Player with input name
    $ Player = Character(name, color="#25ffed", what_size=talkFont)

#starting story.     
    call Chapter1Scene1
    #couunter debug
    scene bg forestroom with fade
    "Counter: mia | [Mia_counter] | silas [Silas_counter] | theo [Theo_counter]|"
    
    #jump to scene 2: the school scene
    call Chapter1Scene2
    #couunter debug
    "Counter: mia | [Mia_counter] | silas [Silas_counter] | theo [Theo_counter]|"
    
    "[Player] went home to rest."
    "Rolling throughout the night, [Player] was unable to sleep, wondering if she should try to find the whereabouts of her sister or take Mia's word to heart."
    stop music
#debug for first decision
#and call the appropriate chapter
    if StoryDecision_Chapter1_Investigate == True:
        
        "chapter1 concluded. decision: Justice" #debug
        "entering chapter2: investigation route"
        call Chapter2Scene2
        "[Player] decided to not give up and walk around town to see if maybe if she can learn anything regarding mia’s job and if it connects to hannah being missing"
        
        
        
        #jump #chapter2 investigate route
        call screen MapScreen
        call Chapter2Scene3_fishing

        #will continue to Chapter2Scene4_helpingSilas
        #continue to afterpuzzle which has 2 possiblel lead. 1 reroute to peaceful route. 
        #or 2 continue investigation route base on Theo counters.

        #current spot afterpuzzle: chapter2scene5
    else: #peaceful school route
        "chapter1 decision: Reflection" #debug

        "Throughout the night, [Player] decided to heed Mia's warning and considered enrolling into [StoryDecision_Chapter1_Schoolname] "
        Player "maybe it is time to just move on and try to live a normal life again."
        Player "well here we are...first day of school."
        window hide
        call screen schoolmapScreen
        
    #call Chapter2Scene2_Aftermath

    #call Chapter2Scene3_fishing
        
    call testlabel #has return completely
    
        

    #
    # End of game
    return

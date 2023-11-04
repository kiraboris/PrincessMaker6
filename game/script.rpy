# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main character and the screen for stats are defined in main_character.rpy


# The game starts here.

screen room_with_imagebuttons(character=None):
    # Add the bg room image to a new layer called "background" at the bottom of the screen.
    imagemap:
        ground "bg room" at center 
        hover "bg room hover" 
        hotspot (1604, 1407, 250 , 100) action Show("e_stats"), SetVariable("b_stats_shown_once", True)
    
    if character is not None:
        add character at center


label start:
        

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "Ardie Son - Citadel.mp3"

    scene bg room with dissolve
    
    show screen room_with_imagebuttons("e happy") 

    e "Hey there! I'm your daughter, Eileen <3"

    default b_stats_shown_once = False
    e "Let's check out my stats by clicking on the book on my right side!"
    
    while not b_stats_shown_once:  #will be set to True in the action trigger when e_stats is shown
        "Click on the book on Eileen's right side to check her stats."

    e "Oh, I'm still level 1..."   
    
    hide screen e_stats
    e "You can check it anytime by clicking on the book on my right side!"   

    jump go_today


label go_today:
    # ask player where to go today
    e "Where shall we go today?"
    hide screen room_with_imagebuttons
    menu: 
        "The park":
            e "Aye! Getting changed for the park!"
            jump park
        "The mall":
            e "Aye! Getting changed for the mall!"
            jump mall
        "The beach":
            e "Aye! Getting changed for the beach!"
            jump beach

label park:
    scene bg park with dissolve
    show e happy at center
    e "We're at the park!"
    return 

label mall:
    scene bg mall with dissolve
    show e plaindress at center
    e "We're at the mall!"
    return 

label beach:
    scene bg beach with dissolve
    show e happy at center
#    show e sad -happy     # hide happy img and show sad img
    e "We're at the beach!"
    return 


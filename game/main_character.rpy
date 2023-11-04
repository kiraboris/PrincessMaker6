# main_character.rpy

define character.e = Character("Eileen")
define e = CharacterStats("e")


## The main character screen 
screen e_stats():
    # Display the character's image
    # add "eileen_small_image"

    # Display the character's name and stats
    frame:
        xalign 0.95
        yalign 0.1
        xpadding 15
        ypadding 8

        vbox:
            spacing 10

            text "Name: [e.name]"
            text "Age: [e.age]"
            text "Weight: [e.weight] kg"
            text "Height: [e.height] cm"
            text "Strength: [e.strength]"
            text "Intelligence: [e.intelligence]"
            text "Charisma: [e.charisma]"
            text "Agility: [e.agility]"
            text "Endurance: [e.endurance]"
            text "Luck: [e.luck]"
            text "Health: [e.health]"
            text "Mana: [e.mana]"
            text "Stamina: [e.stamina]"
            text "Level: [e.level]"
            text "Experience: [e.experience]"

            textbutton "Close":
                action Hide("e_stats")



# Define the eileen_transparent_bg image with a transparent background.
image e happy = "e_happy.png"
image e plaindress = "e_plaindress.png"

# room for the main character
#image bg room = im.Crop(im.Scale("cozy_room_1.png", 1920, 1920), (0, 1920-1080, 1920, 1080))

image bg room =  im.Scale("cozy_room_1.png", 1920, 1920)

image bg room hover = im.Scale("cozy_room_1_buttons.png", 1920, 1920)

image bg park = im.Scale("park.png",  1920, 1920)

image bg mall = im.Scale("mall.png", 1920, 1920)

image bg beach = im.Scale("beach.png",  1920, 1920)

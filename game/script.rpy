init:
    $config.keymap['game_menu'].remove('mouseup_3') #Remove the right click bind from the game menu
    $config.keymap['right_click'] = 'mouseup_3' #Make new right_click keymap and bind it to the right mouse button

# HARD OPENING CREDITS

label start:

    scene black
    $ renpy.pause (1, hard=True)
    show warning with Dissolve(1)
    $ renpy.pause (1)
    hide warning with Dissolve(1)

    jump car1

# SCENE ONE: TRAIN

## Car One

label car1:

    scene car1 with dissolve

    "Player wakes up on train and is spoken to by train employee."
    window hide

    show trainemp1 with dissolve

    trainemp1 "Dialogue..."
    window hide
    hide trainemp1 with dissolve

    "Player will be able to click on the door to enter Car 2"
    window hide

    menu:
        "What should I do? (to be replaced by image buttons)"

        "Enter Car 2.":
            jump car2

## Car Two

label car2:

    scene car2 with dissolve

    "Player will be able to click on the door to enter the Dining Car"

    menu:
        "What should I do? (to be replaced by image buttons)"

        "Enter Dining Car.":
            jump diningcar

## Dining Car

label diningcar:

    scene diningcar with dissolve

    "Player will be able to click on the Train Employee to get something to eat,
    or on Mystery Man to get some hints at how strange the town you're going is..."

    $ renpy.pause()
    jump townext

# SCENE TWO: Town Streets

label townext:

    scene townext with dissolve

    "Here the Player will have the option of going to the Police Station, the Bar,
    the Diner, or to head straight to the mansion."

    menu:
        "Where would you like to go?"

        "Diner":
            jump diner

        "Bar":
            jump bar

        "Head to the Mansion":
            jump mansionext

# SCENE THREE: Diner

## Diner

label diner:

    scene diner with dissolve

    "Here will be a cutscene where the main character reunites with Old Friend,
    talks with Sheriff Tanaka, and is confronted by her old bullies."

    menu:
        "What would you like to do? (to be replaced with image buttons)"

        "Leave":
            jump townext

# SCENE FOUR: Bar

label bar:

    scene barint with dissolve

    "Here will be a cutscene where the main protagonist reunites with her ex-girlfriend
    who she hadn't spoken with for years."

    menu:
        "What would you like to do? (to be replaced with image buttons)"

        "Leave":
            jump townext

# SCENE FIVE: Mansion

## Mansion Exterior

label mansionext:

    scene mansionext with dissolve

    "After a few lines of dialogue, the Player will be able to enter the mansion."

    menu:
        "Enter the Mansion":
            jump mansionint

## Mansion Interior

label mansionint:

    scene mansionint with dissolve

    "Here will be the entry way to explore the house and discover its secrets..."

    $ renpy.pause()
    jump theend

## THE END

label theend:

    scene black with dissolve
    $ renpy.pause (2, hard=True)
    show theend with Dissolve(2)
    $ renpy.pause (3)
    hide theend with Dissolve (2.5)
    $ renpy.pause (2, hard=True)

    #$ renpy.pause (2, hard=True)
    #show theend with Dissolve(2)
    #$ renpy.pause (3)
    #hide theend with Dissolve (2.5)
    #$ renpy.pause (2, hard=True)

    return

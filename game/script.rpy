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
    $ renpy.pause()

    jump car2

## Car Two

label car2:

    scene car2 with dissolve

    "Player will be able to click on the door to enter the Dining Car"

    $ renpy.pause()
    jump diningcar

## Dining Car

label diningcar:

    scene diningcar with dissolve

    "Player will be able to click on the Train Employee to get something to eat,
    or on Mystery Man to get some hints at how strange the town you're going is..."

    $ renpy.pause()
    jump diner

# SCENE TWO: Town Streets

# SCENE THREE: Diner

## Diner

label diner:

    scene diner with dissolve
    $ renpy.pause()
    jump mansionint

# SCENE FOUR: Bar

# SCENE FIVE: Mansion

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

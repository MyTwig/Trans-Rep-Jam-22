# HARD OPENING CREDITS

label start:

    scene black
    $ renpy.pause (1.5, hard=True)
    show warning with Dissolve(2.5)
    $ renpy.pause (5.0)
    hide warning with Dissolve(2.5)

    jump car1

# SCENE ONE: TRAIN

## Car One

label car1:

    scene car1 with dissolve
    $ renpy.pause()
    show trainemp1 with dissolve

    trainemp1 "Dialogue..."
    window hide

    $ renpy.pause()
    hide trainemp1 with dissolve
    $ renpy.pause()
    jump car2

## Car Two

label car2:

    scene car2 with dissolve
    $ renpy.pause()
    jump diningcar

## Dining Car

label diningcar:

    scene diningcar with dissolve
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

    return

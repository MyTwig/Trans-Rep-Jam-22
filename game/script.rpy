# HARD OPENING CREDITS

label start:

    scene black
    $ renpy.pause (1.5, hard=True)
    show warning with Dissolve(2.5)
    $ renpy.pause (5.0)
    hide warning with Dissolve(2.5)

    "Once you add a story, pictures, and music, you can release it to the world!"

    $ renpy.pause (2, hard=True)
    show theend with Dissolve(2)
    $ renpy.pause (3)
    hide theend with Dissolve (2.5)
    $ renpy.pause (2, hard=True)

    return

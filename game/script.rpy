# HARD OPENING CREDITS
init python:

    class Backpack(object):
        def __init__(self):
            self.inventory = []
        def add_item(self, item):
            self.inventory.append(item)
        def get_items(self):
            return self.inventory

default screen_items = ['Bread', 'Calendar', 'Necklace']
default backpack = Backpack()

screen test_grab_screen():

    python:
        
        def show_item(name):
            if name in store.screen_items:
                return True
            else:
                return False
        
        def get_item(drop, drags):
            if not drop:
                return
            print(drags[0].drag_name)
            screen_items.remove(drags[0].drag_name)
            backpack.add_item(drags[0].drag_name)
            if screen_items == []:
                return Return(value=None)
            else:
                renpy.restart_interaction()

    draggroup:

        drag:
            drag_name "Backpack"
            child "backpack.png"
            draggable False
            xpos 800 ypos 750
            dropped get_item
        if show_item("Bread"):
            drag:
                drag_name "Bread"
                child "bread.png"
                droppable False
                xpos 150 ypos 100
                xysize (50, 05)
        if show_item("Calendar"):
            drag:
                drag_name "Calendar"
                child "calendar.png"
                droppable False
                xpos 250 ypos 500
        if show_item("Necklace"):
            drag:
                drag_name "Necklace"
                child "gem-necklace.png"
                droppable False
                xpos 1200 ypos 400


label start:

    scene black
    $ renpy.pause (1, hard=True)
    show warning with Dissolve(1)
    $ renpy.pause (1)
    hide warning with Dissolve(1)

    "Let's test the drag and drop feature"
    call screen test_grab_screen

    "You found some things! Let's see..."
    $ things = backpack.get_items()
    "You got: [things]"

    $ renpy.pause (2, hard=True)
    show theend with Dissolve(2)
    $ renpy.pause (3)
    hide theend with Dissolve (2.5)
    $ renpy.pause (2, hard=True)

    return

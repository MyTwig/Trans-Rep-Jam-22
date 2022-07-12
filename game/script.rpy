# HARD OPENING CREDITS
init python:

    class Backpack(object):
        def __init__(self, max_slots=10):
            self.inventory = []
            self.max_slots = max_slots
            self.used_slots = 0

        def check_for_item(self, item_name):
            #returns the first inventory item that matches and isn't full
            for i in range(len(self.inventory)):
                item = self.inventory[i]
                if (item.item_name == item_name and item.amount != item.stack_size):
                    return item
            return None #We've gone through the whole inventory and there isn't an empty item slot to use

        def add_item_slot(self, item_name, amount, stack_size):
            if self.used_slots == self.max_slots:
                return None
            item = InventoryItem(item_name, amount=amount, stack_size=stack_size)
            self.inventory.append(item)
            self.used_slots += 1
            return True

        def add_item(self, item_name, amount=1, stack_size=1):
            #takes in a string and adds a new InventoryItem to the backpack. Returns True if success, False if backpack is full
            #check if you've grabbed more than one stack_size's worth of this item
            remains = 0
            if self.used_slots == self.max_slots:
                return False
            if (amount > stack_size):
                remains = amount
                while remains >= 0:
                    slot = self.check_for_item(item_name)
                    if slot == None:
                        #We don't have a free slot in the inventory, so let's make one
                        if remains > stack_size:
                            result = self.add_item_slot(item_name, stack_size, stack_size)
                            if result == None:
                                return False #The inventory is full, so we exit the function entirely
                            remains -= stack_size
                        else:
                            result = self.add_item_slot(item_name, remains, stack_size)
                            if result == None:
                                return False #The inventory is full, so we exit the function entirely
                            return True
                    else:
                        #There is a slot, let's see how much fits
                        if stack_size - slot.amount >= remains:
                            #everything will fit
                            slot.add_more(remains)
                            return True
                        else:
                            #Lets top off the stack then and see how much remains
                            remains -= stack_size - slot.amount
                            slot.add_more(slot.stack_size - slot.amount) #Now it's filled up and remains is set accordingly
            else:
                slot = self.check_for_item(item_name)
                if slot == None:
                    #There's no slot currently, so make a new one with the amount gained
                    self.add_item_slot(item_name, amount, stack_size)
                    return True
                else:
                    if slot.stack_size - slot.amount >= amount:
                        #There's enough room in this stack to add the amount grabbed
                        slot.add_more(amount)
                        return True
                    else:
                        remains = amount - (slot.stack_size - slot.amount)
                        slot.add_more(slot.stack_size - slot.amount)
                        result = self.add_item_slot(item_name, remains, stack_size) #Add the leftover into a new stack
                        if result == None:
                            return False #The inventory is full, so we exit the function entirely
                        return True

        def get_items_string(self):
            string = ""
            for i in range(len(self.inventory)):
                string += str(self.inventory[i].item_name)
                if (self.inventory[i].stack_size > 1):
                    #print the number of items in parantheses
                    number = str(self.inventory[i].amount)
                    string += "(" + number + ")"
                if (i != len(self.inventory) - 1):
                    string += ", " #add comma and trailing space if this isn't the last element
            return string

    class InventoryItem(object):
        
        def __init__(self, itemName, amount=1, stack_size=1):
            self.item_name = itemName
            self.amount = amount
            self.stack_size = stack_size
        
        def add_more(self, number_to_add):
            #add items to the stack, returns number of items that couldn't be added by stack
            if (self.amount == self.stack_size):
                return number_to_add
            else:
                if (self.amount + number_to_add > self.stack_size):
                    #We have room, but we can't take it all
                    self.amount += self.stack_size - self.amount
                    return number_to_add - (self.stack_size - self.amount)
                self.amount += number_to_add


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
    #Test that stack size display works by adding two stacks of batteries
    $ backpack.add_item("Batteries", amount=7, stack_size=5)
    call screen test_grab_screen

    "You found some stuff! Let's see..."
    $ things = backpack.get_items_string()
    $slots_used = str(len(backpack.inventory))
    #Print out the batteries and collected loot
    "You have [slots_used] things in your bag: [things]"
    "Here, take some extra batteries with you. They're pretty useful."
    $backpack.add_item("Batteries", amount=4, stack_size=5)
    "You take four batteries." with vpunch
    $slots_used = str(len(backpack.inventory))
    $things = backpack.get_items_string()
    "You have [slots_used] things in your bag: [things]"

    #$ renpy.pause (2, hard=True)
    #show theend with Dissolve(2)
    #$ renpy.pause (3)
    #hide theend with Dissolve (2.5)
    #$ renpy.pause (2, hard=True)

    return

#################

init python:

    class Backpack(object):
        def __init__(self, max_slots=10):
            self.inventory = []
            self.max_slots = max_slots
            self.used_slots = 0
            self.remains = 0

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

        def add_existing_item(self, inventoryItem):
            return self.add_item(inventoryItem.item_name, inventoryItem.amount, inventoryItem.stack_size)

        def add_item(self, item_name, amount=1, stack_size=1):
            #takes in a string and adds a new InventoryItem to the backpack. Returns True if success, False if backpack is full
            #check if you've grabbed more than one stack_size's worth of this item
            if self.used_slots == self.max_slots:
                return False
            if (amount > stack_size):
                self.remains = amount
                while self.remains >= 0:
                    slot = self.check_for_item(item_name)
                    if slot == None:
                        #We don't have a free slot in the inventory, so let's make one
                        if self.remains > stack_size:
                            result = self.add_item_slot(item_name, stack_size, stack_size)
                            if result == None:
                                return False #The inventory is full, so we exit the function entirely
                            self.remains -= stack_size
                        else:
                            result = self.add_item_slot(item_name, self.remains, stack_size)
                            if result == None:
                                return False #The inventory is full, so we exit the function entirely
                            return True
                    else:
                        #There is a slot, let's see how much fits
                        if stack_size - slot.amount >= self.remains:
                            #everything will fit
                            slot.add_more(self.remains)
                            return True
                        else:
                            #Lets top off the stack then and see how much remains
                            self.remains -= stack_size - slot.amount
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
                        self.remains = amount - (slot.stack_size - slot.amount)
                        slot.add_more(slot.stack_size - slot.amount)
                        result = self.add_item_slot(item_name, self.remains, stack_size) #Add the leftover into a new stack
                        if result == None:
                            return False #The inventory is full, so we exit the function entirely
                        return True

        def clear_remains(self):
            self.remains = 0

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

    class ScreenItem(InventoryItem):

        def __init__(self, scene_x, scene_y, inventoryItem):
            self.scene_x = scene_x
            self.scene_y = scene_y
            self.inventoryItem = inventoryItem

        def show_item(self):
            #I'll set this up later to take in a list of variable conditions that must be met before this returns true
            return True



default screen_items = [('Bread', ScreenItem(150, 100, InventoryItem("Bread", 1, 3))), ('Calendar', ScreenItem(250, 500, InventoryItem("Calendar", 1, 1))), ('Necklace', ScreenItem(1200, 400, InventoryItem("Necklace", 1, 1)))]
default backpack = Backpack()

screen test_grab_screen():

    python:

        def get_item(drop, drags):
            for itemTuple in screen_items:
                if itemTuple[0] == drags[0].drag_name:
                    item_tuple = itemTuple
            if not drop:
                drags[0].snap(item_tuple[1].scene_x, item_tuple[1].scene_y, 0.1)
                return
            else:
                #The first element of the tuple is the item name, and the drag element is named after the item
                itemFits = backpack.add_existing_item(item_tuple[1].inventoryItem) #Add the inventory item to the backpack from the ScreenItem and check if it fits
                if itemFits:
                    screen_items.remove(item_tuple) #We have picked up all of the items and should take it off the list
                else:
                    itemTuple[1].amount = backpack.remains #Set the amount left in the scene to what the backpack couldn't hold
                    return Return(value=None) #Screen closes and value should be changed to reflect that the backpack is full now

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

        for item in screen_items:
            if item[1].show_item():
                drag:
                    drag_name item[0]
                    child item[1].inventoryItem.item_name.lower() + ".png" #Ignore case as filenames are all lowercase so far
                    droppable False
                    xpos item[1].scene_x ypos item[1].scene_y



# <<<<<<< HEAD

# =======

#    "Let's test the drag and drop feature"
#    # Test that stack size display works by adding two stacks of batteries
#    $ backpack.add_item("Batteries", amount=7, stack_size=5)
#    call screen test_grab_screen

#    "You found some stuff! Let's see..."
#    $ things = backpack.get_items_string()
#    $slots_used = str(len(backpack.inventory))
#    # Print out the batteries and collected loot
#    "You have [slots_used] things in your bag: [things]"
#    "Here, take some extra batteries with you. They're pretty useful."
#    $backpack.add_item("Batteries", amount=4, stack_size=5)
#    "You take four batteries." with vpunch
#    $slots_used = str(len(backpack.inventory))
#    $things = backpack.get_items_string()
#    "You have [slots_used] things in your bag: [things]"


# >>>>>>> 363c85e4855e981a1d4c40aa50530e312adc7f9e

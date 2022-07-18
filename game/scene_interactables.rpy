init python:

    class ScreenInteractable(object):
        """Base class for scene elements that can be clicked"""

        def __init__(self, id, idle_image, hover_image, on_click_action, alt_hover_images=None):
            self.id = id
            self.idle_image = idle_image
            self.hover_image = hover_image
            self.on_click_action = on_click_action
            self.alt_hover_images = alt_hover_images

        def OnClick(self, params = None):
            """Runs the stored click action if it exists with an optional list of parameters"""
            if self.on_click_action == None:
                return None #There is no function to run, so return nothing
            if params not None:
                return self.on_click_action(params)
            else
                return self.on_click_action()
        
        def __eq__(self, other):
            return self.id == other.id
    
    class Location(ScreenInteractable):
        """Elements that change the character's location when clicked. A list of flag/bool tuples can be passed as requirements and the location will be marked as locked until all flags match in store.flags."""

        def __init__(self, id, idle_image, hover_image, on_click_action, alt_hover_images=None, requirements=None, interact_when_locked=False, locked_click_action=None):
            super().__init__(id, idle_image, hover_image, on_click_action, alt_hover_images)
            self.requirements = requirements
            if requirements not None:
                self.locked = self.RequirementsMet()
            else:
                self.locked = False
            self.interact_when_locked = interact_when_locked
            self.locked_click_action = locked_click_action

        def RequirementsMet(self):
            if requirements == None:
                return True #There are no requirements, so of course you have met them
            for i in range(0, len(self.requirements)):
                if self.requirements[i][0] in store.flags:
                    #Check that the required flag exists in the dictionary
                    if store.flags[self.requirements[i][0]] != self.requirements[i][1]:
                        #If the flag exists but the value doesn't match, then this location is locked
                        return False
                else:
                    #If the flag doesn't exist then the location should be locked
                    return False
            #If all of the required flags exist and match, then the location is unlocked
            return True
        
        def OnClick(self, params=None):
            if locked:
                if self.interact_when_locked && self.locked_click_action != None:
                    return self.locked_click_action(params) #Pass back any value from the action function
                else
                    return None #Don't interact if its locked
            else:
                return super().OnClick(params)
    
    class ScreenCharacter(ScreenInteractable):
        """A placeholder class for characters that can be clicked"""
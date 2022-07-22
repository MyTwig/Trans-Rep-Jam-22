init python:

    class ScreenInteractable(object):
        """Base class for scene elements that can be clicked"""

        def __init__(self, name, image_button, on_click_action, on_alt_click=None, info_text=None):
            self.name = name
            self.image_button = image_button
            self.on_click_action = on_click_action
            self.on_alt_click = on_alt_click
            self.information_text = info_text

        def OnClick(self, params = None):
            """Runs the stored click action if it exists with an optional list of parameters"""
            if self.on_click_action == None:
                return None #There is no function to run, so return nothing
            if params != None:
                return self.on_click_action(params)
            else:
                return self.on_click_action()
        
        def OnAltClick(self, params = None):
            """If there is an alt_click function call it and return the value when right clicked"""
            if on_alt_click:
                if params:
                    return on_alt_click(params)
                else:
                    return on_alt_click()
            else:
                return None

        def __eq__(self, other):
            return self.name == other.name
    
    class Location(object):

        def __init__(self, screen_interactable, requirements=None, interact_when_locked=False, locked_click_action=None):
            self.screen_interactable = screen_interactable
            self.requirements = requirements
            if requirements !=   None:
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
                if self.interact_when_locked and self.locked_click_action != None:
                    return self.locked_click_action(params) #Pass back any value from the action function
                else:
                    return None #Don't interact if its locked
            else:
                return self.screen_interactable.OnClick(params)
    
    class ScreenCharacter(object):
        """A placeholder class for characters that can be clicked"""
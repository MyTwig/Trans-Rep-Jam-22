#A list of all base items in the game, descriptions, combinations, etc.
init python:
    items = {} #Create a dictionary with item name as key and InventoryItem as the value
    items['drivers_license'] = InventoryItem("Driver's License", itemID="drivers_license", description_text="My driver's license. I've got to renew it in a few months...")
    items['caretaker_letter'] = InventoryItem("Letter From CARETAKER'S NAME", itemID='caretaker_letter', description_text="Addressed to MAIN, with an official looking seal on it. The return address looks familiar.")
    items['lighter'] = InventoryItem("Lighter", description_text="Some of the flag decal has worn off, but it's still a good lighter.")
    items['cigarettes'] = InventoryItem("Pack of Cigarettes", itemID='cigarettes', description_text="SURGEON GENERAL'S WARNING: Smoking Causes Lung Cancer, Heart Disease, Emphysema, and May Complicate Pregnancy.\nQuitting Smoking Now Greatly Reduces Serious Risks to Your Health.")
    items['silver_key'] = InventoryItem("Silver Key", itemID='silver_key', description_text="A small, ornate silver key. It's surprisingly cool to the touch.")
    items['journal'] = InventoryItem("Journal", description_text="A little worn and full of notes.")
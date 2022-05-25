from glob import glob
import Classes

itemStore = Classes.itemStore
inputs = Classes.Inputs

def start():
    global itemStore
    global inputs
    
    isRunning = True
    
    while isRunning:
        itemStore.load(True)
        
        id = int(inputs.prepareForNumberInput("\nPlease enter product ID: "))
        
        print("\nYou have selected the item: " + str(itemStore.items[id].name))
        
        if not inputs.prepareToContinue("Is this the correct item? y/n: "):
            continue
        else:
            quantity = inputs.prepareForNumberInput("\nHow many products would you like?: ")
    
start()
from glob import glob
import Classes

itemStore = Classes.itemStore
inputs = Classes.Inputs

def start():
    global itemStore
    global inputs
    
    itemStore.load(True)
    
    id = inputs.prepareForNumberInput("\nPlease enter product ID: ")
    quantity = inputs.prepareForNumberInput("\nHow many products would you like?: ")
    
start()
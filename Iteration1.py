import Classes
import logging
import pathlib

# read = "r"
# append = "a"
# write = "w"
# create = "x"
# text = "t"
# binary = "b"

itemStore = Classes.ItemStore()
path = pathlib.Path(__file__).parent.resolve()
    
def prepareToContinue():
    
    firstCondition = False
    secondCondition = False
    
    while not firstCondition or not secondCondition:
        
        userInput = str(input("Please enter y/n: "))
        
        logging.debug("user input: " + str(userInput))
        logging.debug("condition 1: " + str(firstCondition))
        logging.debug("condition 2: " + str(secondCondition))
        
        firstCondition = userInput in ["y", "Y"]
        secondCondition =  userInput in ["n", "N"]
        
        if firstCondition:
            return True
        elif secondCondition:
            return False
        else:
            print("Please enter a valid input.")
    
    
def add():
    global itemStore
    
    isAdding = True

    with open(str(str(path) + "Stockpile.txt"), "w") as f:
        while isAdding == True:
            nameInput = str(input("What item would you like to add?: "))
            quantityInput = int(input("How many items are you adding?: "))
            priceInput = float(input("How much does this item cost?: "))
    
            item = itemStore.addItem(nameInput, 
                                     quantityInput, 
                                     priceInput)
        
            isAdding = prepareToContinue()
            
        items = itemStore
            
        f.writelines(str(items.toJSON()))    
    
        f.close

def start():
    
    try:
        open(str(str(path) + "Stockpile.txt"), "x")
    except:
        print("Stocklist file already exists")
    
    add()

    print(str(itemStore.items))
    
start()


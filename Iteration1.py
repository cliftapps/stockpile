import Classes
import logging

# read = "r"
# append = "a"
# write = "w"
# create = "x"
# text = "t"
# binary = "b"

itemStore = Classes.ItemStore()
    
def prepareToContinue():
    
    firstCondition = False
    secondCondition =  False
    
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

    with open("Stockpile/stockpile.txt", "w") as f:
        while isAdding == True:
            nameInput = str(input("What item would you like to add?: "))
            quantityInput = int(input("How many items are you adding?: "))
    
            item = itemStore.addItem(nameInput, quantityInput)
        
            isAdding = prepareToContinue()
            
        items = itemStore
            
        f.writelines(str(items.toJSON()))    
    
        f.close

def start():
    
    try:
        with open("Stockpile/stockpile.txt", "x") as f:
            f.close
    except:
        print("Stocklist file already exists")
    
    add()

    print(str(itemStore.items))
    print(itemStore.toJSON())
    
start()


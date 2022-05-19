import Classes
import logging

itemStore = Classes.ItemStore()

def prepare(value):
    logging.debug(value)
    
def prepareToContinue():
    
    firstCondition = False
    secondCondition =  False
    
    while not firstCondition or not secondCondition:
        
        userInput = str(input("Please enter yes or no: ")).casefold
    
        y = 'y'.casefold
        n = 'n'.casefold
        yes = 'yes'.casefold
        no = 'no'.casefold
        
        logging.debug("y: " + str(y) + "\nn: " + str(n) + "\nyes: " + str(yes) + "\nno: " + str(no))
        logging.debug("user input: " + str(userInput))
        logging.debug("condition 1: " + str(firstCondition))
        logging.debug("condition 2: " + str(secondCondition))
        
        firstCondition = userInput == y or userInput == yes
        secondCondition =  userInput == n or userInput == no
        
        if firstCondition:
            return True
        elif secondCondition:
            return False
        else:
            print("Please enter a valid input.")
    
    
def add():
    global itemStore
    
    isAdding = True

    with open("./stockpile.txt", "w") as f:
        while isAdding == True:
            nameInput = str(input("What item would you like to add?: "))
            quantityInput = int(input("How many items are you adding?: "))
    
            item = itemStore.addItem(nameInput, quantityInput)
        
            isAdding = prepareToContinue()
            
        items = itemStore
            
        f.writelines(str(items.toJSON()))    
    
        f.close

def start():
    
    add()

    print(str(itemStore.items))
    
start()


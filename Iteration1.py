import Classes

itemStore = Classes.ItemStore()

def prepare(value):
    print(value)
    
def prepareToContinue():
    userInput = str(input("Please enter yes or no: ")).lower
    
    userInput = str(userInput)
    
    y = 'y'
    n = 'n'
    yes = 'yes'
    no = 'no'
    
    firstCondition = userInput == y or userInput == yes
    secondCondition =  userInput == n or userInput == no
    
    print("y: " + str(y) + "\nn: " + str(n) + "\nyes: " + str(yes) + "\nno: " + str(no))
    print("user input: " + str(userInput))
    print("condition 1: " + str(firstCondition))
    print("condition 2: " + str(secondCondition))
    
    while not firstCondition or not secondCondition:
        if firstCondition:
            return True
        elif secondCondition:
            return False
        else:
            print("Please enter a valid input.")
            
            userInput = str(input("Please enter yes or no: ")).lower
            
            userInput = str(userInput)
            
            print("y: " + str(y) + "\nn: " + str(n) + "\nyes: " + str(yes) + "\nno: " + str(no))
            print("user input: " + str(userInput))
            print("condition 1: " + str(firstCondition))
            print("condition 2: " + str(secondCondition))
    
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


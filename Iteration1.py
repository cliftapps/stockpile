from gc import get_threshold
import Classes
import math

# read = "r"
# append = "a"
# write = "w"
# create = "x"
# text = "t"
# binary = "b"

itemStore = Classes.ItemStore()
    
def prepareToContinue():
    
    firstCondition = False
    secondCondition = False
    
    while not firstCondition or not secondCondition:
        
        userInput = str(input("Please enter y/n: "))
        
        firstCondition = userInput in ["y", "Y"]
        secondCondition = userInput in ["n", "N"]
        
        if firstCondition:
            return True
        elif secondCondition:
            return False
        else:
            print("Please enter a valid input.")
            
def prepareForStrInput(message: str):
    error = True
    userInput: str
    
    while error == True:
            
        try:
            userInput = str(input(message))
        
        except:
            print("Please enter a valid input")
            
        if userInput.__len__() == 0:
            print("No input detected, try again")
        else:
            error = False
           
    return userInput

def prepareForNumberInput(message: str):
    error = True
    value = 0
    
    while error == True:
        userInput = input(message)
            
        try:
            value = float(userInput)
            
        except UnboundLocalError:
            print("Please enter valid value")
            
            continue
        
        except ValueError:
            print("Please enter a number")
            
            continue
            
        error = False
        
    return value

    
def add():
    global itemStore
    
    isAdding = True

    while isAdding == True:
        
        nameInput = prepareForStrInput("Please enter what item you wish to add: ")
        quantityInput = prepareForNumberInput("How many items are you adding?: ")
        priceInput = prepareForNumberInput("How much does this item cost?: ")
        
        priceInputFormatted = float("{:.2f}".format(float(priceInput)))

        item = itemStore.addItem(nameInput, 
                                int(float(quantityInput)), 
                                priceInputFormatted)
        
        itemStore.save()
    
        isAdding = prepareToContinue()

def start():
    
    try:
        open(itemStore.path, "x")
    except:
        
        print("Loaded stocklist")
        
        try:
            itemStore.load()
        except:
            print("No data found")
        
        
    
    add()
    
def login():
    security = Classes.Security()

    while not security.isAuthenticated:
        username = str(input("Please enter your username: "))
        password = str(input("Please enter your password: "))
        
        security.login(username, password)
        
        if security.isAuthenticated:
            start()
        else:
            print("Invalid login, please enter the correct username or password!")
    
login()


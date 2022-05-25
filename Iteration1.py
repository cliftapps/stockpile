from gc import get_threshold
import Classes
import math

# read = "r"
# append = "a"
# write = "w"
# create = "x"
# text = "t"
# binary = "b"

itemStore = Classes.itemStore
inputs = Classes.Inputs
    
def add():
    global itemStore
    global inputs
    
    isAdding = True

    while isAdding == True:
        
        nameInput = inputs.prepareForStrInput("Please enter what item you wish to add: ")
        quantityInput = inputs.prepareForNumberInput("How many items are you adding?: ")
        priceInput = inputs.prepareForNumberInput("How much does this item cost?: ")
        
        priceInputFormatted = float("{:.2f}".format(float(priceInput)))

        item = itemStore.addItem(nameInput, 
                                int(float(quantityInput)), 
                                priceInputFormatted)
        
        itemStore.save()
    
        isAdding = inputs.prepareToContinue()

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


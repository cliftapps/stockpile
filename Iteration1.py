# This file needs to be able to manipulate the itemStore and have access to inputs

import Classes

# Variables are declared global to reduce the length of references used in the Iteration 1 methods.

itemStore = Classes.itemStore
inputs = Classes.Inputs
    
# Add function is responsibile for adding items to the stocklist.
    
def add():
    # Global variables need to be referenced in python methods, otherwise errors will incure.
    
    global itemStore
    global inputs
    
    # 'isAdding' indicates whether the user is still adding items or not.
    # Once the condition is false, the loop will be broken.
    
    isAdding = True

    while isAdding == True:
        
        # All inputs go through prepare static methods within 'Classes.Inputs'.
        # If the inputs meet the correct criteria, they will be assigned to the variables declared below.
        # The variables will not be assigned until an input is correct.
        
        nameInput = inputs.prepareForStrInput("\nPlease enter what item you wish to add: ")
        
        # The 'isZeroAllowed' indicates whether an input of zero is allowed.
        # In some cases it is acceptable, so having the ability to set this alleviates the need for further methods.
        # DON'T REPEAT CODE!
        
        quantityInput = inputs.prepareForNumberInput("How many items are you adding?: ", isZeroAllowed = False)
        priceInput = inputs.prepareForNumberInput("How much does this item cost?: ")
        
        # Once all valid inputs are inputted, the price is formatted to two decimal places. 
        # The item can then be added with a valid currency value.
        
        priceInputFormatted = float("{:.2f}".format(float(priceInput)))
        
        # All inputs has now been validated, now an item can be added and it won't contain data that is not supposed to be there.

        item = itemStore.addItem(nameInput, 
                                int(float(quantityInput)), 
                                priceInputFormatted)
        
        # The save function in the itemStore saves all the items to the text file in a JSON format.
        
        itemStore.save()
        
        # 'prepareToContinue' returns a True of false value depending on where 'y' or 'n' is inputted.
        # False ends the loop ('n').
        # True continues the loop ('y').
    
        isAdding = inputs.prepareToContinue("Would you like to add more items? y/n: ")
        
# This starts the stock addition flow.

def start():
    
    # This prints the title of the stock addtion flow.
    
    print("\n--Add Stock--")
    
    # This creates the stocklist.
    # If the stocklist exists, it will load the stocklist.
    
    try:
        open(itemStore.path, "x")
    except:
        
        print("\nLoaded stocklist")
        
        try:
            # If the stocklist is empty, it will not load the file to prevent JSON decoding error.
            
            itemStore.load()
        except:
            print("\nNo data found")
            
    # Runs 'add()' method.
        
    add()


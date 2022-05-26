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
        
        nameInput = inputs.prepareForStrInput("\nPlease enter what item you wish to add: ")
        quantityInput = inputs.prepareForNumberInput("How many items are you adding?: ", isZeroAllowed = False)
        priceInput = inputs.prepareForNumberInput("How much does this item cost?: ")
        
        priceInputFormatted = float("{:.2f}".format(float(priceInput)))

        item = itemStore.addItem(nameInput, 
                                int(float(quantityInput)), 
                                priceInputFormatted)
        
        itemStore.save()
    
        isAdding = inputs.prepareToContinue("Would you like to add more items? y/n: ")

def start():
    
    print("\n--Add Stock--")
    
    try:
        open(itemStore.path, "x")
    except:
        
        print("\nLoaded stocklist")
        
        try:
            itemStore.load()
        except:
            print("\nNo data found")
        
    add()


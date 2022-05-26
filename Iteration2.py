# The iteration requires manipulation of the itemStore class and methods within the Inputs class to function correctly.

import Classes

# Instances/classes are referenced globally to shorten references.
# Same instance of itemStore has to be used over both iterations.
# A different instance would lead to unrelated entries in the stocklist.txt file.

itemStore = Classes.itemStore
inputs = Classes.Inputs

def start():
    # Global variables need to be referenced in the top of a method so the program does not throw errors.
    
    global itemStore
    global inputs
    
    # isRunning is a boolean value that indicates whether the iteration is still running or not.
    
    isRunning = True
    
    # Used as a shorter version of: str(itemStore.items[id].name) to improve readability and reduce key presses.
    
    name: str
    
    # Title of iteration is printed on the console.
    
    print("\n--Order Stock--")
    
    while isRunning:
        # Calls the itemStore load function that grabs and decodes JSON from stocklist.txt.
        # The boolean idicates whether the stocklist should be printed in a readable format in the console.
        # As this iteration requires an overview of all the stock so isItemListPrinted is set to True.
        
        itemStore.load(isItemListPrinted = True)
        
        # User is prompted to enter the ID of a product to start the order flow.
        
        id = int(inputs.prepareForNumberInput("\nPlease enter product ID: "))
        
        # This try/except statement checks that a valid index is inputted for the item.
        # The item indexes match with the item IDs, so if an index is out of range we know the product does not exist.
        # This would be problematic if items were to be removed, however it is merely indicated they are out of stock and users can't order them.
        
        try:
            name = str(itemStore.items[id].name)
            price = "£" + str(itemStore.items[id].price)
        except:
            print("\nPlease enter a valid product id")
            
            continue
        
        # This checks the 'hasStock' attribute of the item that was selected via it's unique identifier.
        # If the quantity of the item is 0, 'hasStock' will have been set to false.
        # Users will be prompted that the item is out of stock and taken back to the start of the order process.
        
        if not itemStore.items[id].hasStock:
            print("\nSorry, this item is out of stock :(")
            
            continue
        
        # Now the user is given brief information on the item they have chosen
        
        print("\nYou have selected the item: " + name)
        print("\nThe price of a " + name + " is: " + price)
        
        # A user can confirm if they have selected the right item.
        # If they input 'y' they will be able to further progress with the order.
        # If they input 'n' they will be sent back to the beginning to get the item they really wanted.
        
        if not inputs.prepareToContinue("\nIs this the correct item? y/n: "):
            continue
        else:
            # Great, the user has selected the right item.
            # Now the user is asked how many items they want to order.
            
            quantity = inputs.prepareForNumberInput("\nHow many products would you like?: ", False)
            
            # If they input a greater quantity than the quantity of the item, they will be presented with an error and sent to the beginning.
            
            if quantity > itemStore.items[id].quantity:
                print("\nNot enough stock, there are only " + str(int(itemStore.items[id].quantity)) + " " + name + "s")
                
                continue
            
            # If the quantity is equal to or below the quantity of the selected item in the stocklist,
            # The user will be presented with the total cost of their purchase.
            
            print("\nThe total of you purchase is: £" + str(itemStore.items[id].price * quantity))
            
            # They are then asked if they wanted to process with the purchase.
            # If 'y' is inputted, then they will be informed that the order has been processed, 
            # and they are given a breakdown of their order.
            # If 'n' is selected, they will be prompted that the order was cancelled and be returned to the beginning of the order flow.
            
            if inputs.prepareToContinue("\nWould you like to proceed this purchase? y/n: "):
                
                # This is a method in the itemStore that handles the purchase of the item.
                # It will update the 'itemStore.items' array and save it to the stocklist.txt.
                # The is is used to reference the item the user has selected, and the qauntity is subtracted off the quantity of the item the user wants to purchase.
                
                itemStore.buyItem(id, quantity)

                # Prints overvier of the order.
                
                print("\nYour order has been processed!")
                print(" Item name: " + name)
                print(" Items purchased: " + str(int(quantity)))
                print(" Total price: £" + str(itemStore.items[id].price * quantity))
                
                # Determines whether a user wants to order more items or return to the 'login' method in the 'Main' file.
                
                isRunning = inputs.prepareToContinue("\nWould you like to purchase more items? y/n: ")
            else:
                # Statement is executed if user does not want to proceed with order.
                
                print("\nYour order has been cancelled.")
                    
            
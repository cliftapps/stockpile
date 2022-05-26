from glob import glob
import Classes

itemStore = Classes.itemStore
inputs = Classes.Inputs

def start():
    global itemStore
    global inputs
    
    isRunning = True
    name: str
    
    while isRunning:
        itemStore.load(True)
        
        id = int(inputs.prepareForNumberInput("\nPlease enter product ID: "))
        
        try:
            name = str(itemStore.items[id].name)
            price = "£" + str(itemStore.items[id].price)
        except:
            print("Please enter a valid product id")
            
            continue
        
        if not itemStore.items[id].hasStock:
            print("Sorry, this item is out of stock :(")
            
            continue
        
        print("\nYou have selected the item: " + name)
        print("\nThe price of a " + name + " is: " + price)
        
        if not inputs.prepareToContinue("\nIs this the correct item? y/n: "):
            continue
        else:
            quantity = inputs.prepareForNumberInput("\nHow many products would you like?: ")
            
            print("\nThe total of you purchase is: £" + str(itemStore.items[id].price * quantity))
            
            if inputs.prepareToContinue("\nWould you like to proceed this purchase? y/n: "):
                
                itemStore.buyItem(id, quantity)
                
                print("\nYour order has been processed!")
                print(" Item name: " + name)
                print(" Items purchased: " + str(quantity))
                print(" Total price: £" + str(itemStore.items[id].price * quantity))
                
                isRunning = inputs.prepareToContinue("\nWould you like to purchase more items? y/n: ")
            
    print("Program ended.")
    
start()
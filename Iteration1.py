import ItemStore

itemStore = ItemStore.ItemStore()

def prepare(value):
    print(value)
    
def prepareToContinue(input):
    print(input)
    
    if input == 'y' or input == 'yes':
        return True
    else:
        return False
    
def add():
    global itemStore
    
    isAdding = True

    with open("./stockpile.txt", "w") as f:
        while isAdding == True:
            nameInput = str(input("What item would you like to add?: "))
            quantityInput = int(input("How many items are you adding?: "))
    
            item = itemStore.addItem(nameInput, quantityInput)
        
            isAdding = prepareToContinue(prepare(str(input("Do you wish to continue?: "))))
            
        items = itemStore
            
        f.writelines(str(items.toJSON()))    
    
        f.close

def start():
    
    add()

    print(str(itemStore.items))
    
start()


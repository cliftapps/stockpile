import json
from uuid import UUID

# As there is no registration flow, the user class is set-up to be created with all its attributes already established. 
# A UUID has been used to futureproof the program, just incase a registration flow is implemented.

class User:
    id: UUID
    username: str
    password: str
    
    # This initializes the class, each attribute is set within the class.
    
    def __init__(self):
        self.id = UUID()
        self.username = "admin"
        self.password = "password"
        
# The 'Item' class is used as a blue print to identify each individual item.

class Item:
    id: int
    name: str
    quantity: int
    
    # Whenever an item is created it required an id, name and quantity.
    # These are inputted when and where the instance is created.
    
    def __init__(self, id, name, quantity):
        
        self.id = id
        self.name = name
        self.quantity = quantity
        
# The 'ItemStore' class is used to manage items.
# When it is defined, users can create and remove items.
# This updates an array of 'Item(s)' which can then be encoded to JSON.

class ItemStore:
    # A shorter way of using: 
    #   items: [Item] 
    # 
    #   __init__(self): 
    #       self.items = [Item]
    #
    # It creates an empty array of items.
    
    items = [Item]
    
    # Once an instance of 'ItemStore' has been established, this method can be utilised.
    #
    
    def addItem(self, name, quantity):
        
        item = Item(name, quantity)
        
        self.items.append(item)
        
        item.id = self.items.index(item)
        
        return item
    
    def removeItem(self, index):
        
        self.items.remove(self.items[index])
        
    def toJSON(self):
        
        return json.dumps(self.items, 
                          default=lambda 
                          o: o.__doc__ ,   
                          sort_keys=True, 
                          indent = 4)
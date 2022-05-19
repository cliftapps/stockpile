import json
from uuid import UUID

# You will notice that in each of the methods used in a class, the instance of that class defined is added to each method automatically.
# To reference this instance 'self' is needed.
# This will allow the method to manipulate attributes within the class as well as utilise other methods within the class.

# As there is no registration flow, the user class is set-up to be created with all its attributes already established. 
# A UUID has been used to futureproof the program, just incase a registration flow is implemented.

class User:
    id: UUID
    username: str
    password: str
    
    # This initializes the class, each attribute is set within the class.
    
    def __init__(self, username: str, password: str):
        self.id = UUID()
        self.username = username
        self.password = password
        
# The security class is used to managed user logins.

class Security:
    # The expected instance of user is created here
    
    user = User()
    
    def login(self, user: User):
        
        if self.user.username == user.username & self.user.password == user.password:
            return True
        else:
            return False
            
            
 # The 'Item' class is used as a blue print to identify each individual item.

class Item:
    id: int
    name: str
    quantity: int
    
    # Whenever an item is created it required an id, name and quantity.
    # These are inputted when and where the instance is created.
    
    def __init__(self, name, quantity):

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
    # It involves creating an instance of an item usings values established from a users input, appending that item onto the 'items' attribute and then defining its id based on its index position.
    # The item is also returned so it can be used immediately after it is created.
    
    def addItem(self, name, quantity):
        
        item = Item(name, quantity)
        
        self.items.append(item)
        
        item.id = self.items.index(item)
        
        return item
    
    # This allows for the removal of items when 'ItemStore' has been instantiated.
    # The method takes an index and removes the 'Item' situated at that index.
    
    def removeItem(self, index):
        
        self.items.remove(self.items[index])
        
    # This encodes the array of 'Item(s)' that have been established.
    # This will get called everytime there is an update to the store so the stock list never becomes outdated.
        
    def toJSON(self):
        
        return json.dumps(self.items, 
                          default=lambda 
                          o: o.__doc__ ,   
                          sort_keys=True, 
                          indent = 4)
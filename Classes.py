import json
from uuid import UUID
import pathlib

# You will notice that in each of the methods used in a class, the instance of that class defined is added to each method automatically.
# To reference this instance 'self' is needed.
# This will allow the method to manipulate attributes within the class as well as utilise other methods within the class.

# As there is no registration flow, the user class is set-up to be created with all its attributes already established. 

class User:
    id: int
    username: str
    password: str
    
    # This initializes the class, each attribute is set within the class.
    
    def __init__(self):
        self.id = 1
        self.username = "admin"
        self.password = "password"
        
# The security class is used to managed user logins.

class Security:
    # The expected instance of user is created here
    
    user = User()
    
    def login(self, username: str, password: str):
        
        # UUID is not needed here as there is only one user for this system.
        
        if self.user.username == username & self.user.password == password:
            return True
        else:
            return False
            
            
 # The 'Item' class is used as a blue print to identify each individual item.

class Item:
    id: int
    name: str
    quantity: int
    price: float
    
    # Whenever an item is created it required an id, name and quantity.
    # These are inputted when and where the instance is created.
    
    def __init__(self, name, quantity, price):

        self.name = name
        self.quantity = quantity
        self.price = price
        
# The 'ItemStore' class is used to manage items.
# When it is defined, users can create and remove items.
# This updates an array of 'Item(s)' which can then be encoded to JSON.

class ItemStore:
    # Creates an empty array for instances of 'Item'
    
    items = []
    
    path = str(pathlib.Path(__file__).parent.resolve() ) + "/Stockpile/Stockpile.txt"
    
    # Once an instance of 'ItemStore' has been established, this method can be utilised.
    # It involves creating an instance of an item usings values established from a users input, appending that item onto the 'items' attribute and then defining its id based on its index position.
    # The item is also returned so it can be used immediately after it is created.
    
    def addItem(self, name, quantity, price):
        
        item = Item(name, quantity, price)
        
        self.items.append(item)
        
        item.id = self.items.index(item)
        
        return item
    
    # This allows for the removal of items when 'ItemStore' has been instantiated.
    # The method takes an index and removes the 'Item' situated at that index.
    
    def removeItem(self, index):
        
        self.items.remove(self.items[index])
        
    # This encodes the array of 'Item(s)' that have been established.
    # This will get called everytime there is an update to the store so the stock list never becomes outdated.
        
    def save(self):
        with open(self.path, "w") as f:
            
            f.writelines(str(json.dumps({"stock": [item.__dict__ for item in self.items]}, indent = 2)))
            
        print(self.items)
            
    def load(self):
        with open(self.path, "r") as f:
            
            list = f.readlines()
            
            string = ''.join(list)
            
            data = json.loads(string)
            
            for item in data['stock']:
                
                self.addItem(item['name'],
                             item['quantity'],
                             item['price'])
                
        print(self.items)
        
import json
from uuid import UUID
import pathlib

# You will notice that in each of the methods used in a class, the instance of that class defined is added to each method automatically.
# To reference this instance 'self' is needed.
# This will allow the method to manipulate attributes within the class as well as utilise other methods within the class.

# As there is no registration flow, the user class is set-up to be created with all its attributes already established.

class Inputs:
    
    @staticmethod
    def prepareToContinue(message: str = "Please enter y/n: "):
        
        firstCondition = False
        secondCondition = False
        
        while not firstCondition or not secondCondition:
            
            userInput = str(input(message))
            
            firstCondition = userInput in ["y", "Y"]
            secondCondition = userInput in ["n", "N"]
            
            if firstCondition:
                return True
            elif secondCondition:
                return False
            else:
                print("Please enter a valid input.") 
    
    @staticmethod            
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

    @staticmethod
    def prepareForNumberInput(message: str, isZeroAllowed: bool = True):
        error = True
        value = 0
        
        while error == True:
            userInput = input(message)
                
            try:
                value = float(userInput)
                
            except ValueError:
                print("Please enter a number")
                
                continue
            
            
            if value < 0:
                print("Please enter a positive number")
                
                continue
            
            if not isZeroAllowed:
                if value == 0 :
                    print("Please enter a number more than zero")
                
                    continue
                
            error = False
            
        return value

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
    isAuthenticated = False
    
    def login(self, username: str, password: str):
        
        if self.user.username == username and self.user.password == password:
            self.isAuthenticated = True
        else:
            self.isAuthenticated = False
            
    def logout(self):
        self.isAuthenticated = False
        
        print("\nUser " + self.user.username + " has been logged out!")

            
            
 # The 'Item' class is used as a blue print to identify each individual item.

class Item:
    id: int
    name: str
    quantity: int
    price: float
    hasStock: bool
    
    # Whenever an item is created it required an id, name and quantity.
    # These are inputted when and where the instance is created.
    
    def __init__(self, name, quantity, price):

        self.name = name
        self.setQuantity(quantity)
        self.price = price
        
    def setQuantity(self, value: int):
        self.quantity = value
        self.hasStock = value != 0
        
        return self.hasStock
        
# The 'ItemStore' class is used to manage items.
# When it is defined, users can create and remove items.
# This updates an array of 'Item(s)' which can then be encoded to JSON.

class ItemStore:
    # Creates an empty array for instances of 'Item'
    
    items = []
    
    path = str(pathlib.Path(__file__).parent.resolve() ) + "/Stockpile.txt"
    
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
            
    def load(self, isListed: bool = False):
        self.items.clear()
        
        with open(self.path, "r") as f:
            
            list = f.readlines()
            
            string = ''.join(list)
            
            data = json.loads(string)
            
            for item in data['stock']:
                
                self.addItem(item['name'],
                             item['quantity'],
                             item['price'])
                
            if isListed:
                print("\nCurrent stock:")
            
                for item in data['stock']:
                    
                    print("\nID: " + str(item['id']))
                    if item['hasStock']:
                        print(" Item name: " + item['name'])
                        print(" Item quantity: " + str(int(item['quantity'])))
                        print(" Item price: £" + str(item['price']))
                    else:
                        print(" Item out of stock! Sorry :(")
                
    def buyItem(self, id, quantity: int):
        isBuyingItem = True
        item: Item = self.items[id]
        
        while isBuyingItem:

            item.quantity -= quantity
            
            item.setQuantity(item.quantity)
            
            isBuyingItem = False
            
        if not isBuyingItem:
            self.save()
    
itemStore = ItemStore()
        
import json
from uuid import UUID
import pathlib

# You will notice that in each of the methods used in a class, the instance of that class defined is added to each method automatically.
# To reference this instance 'self' is needed.
# This will allow the method to manipulate attributes within the class as well as utilise other methods within the class.

# Inputs are used all over both iterations, there will only ever need to be one version of these inputs.
# @staticmethod allows the methods to be accesses without the class being instantiated.

class Inputs:
    
    @staticmethod
    def prepareToContinue(message: str = "Please enter y/n: "):
        
        # Method assumes input is false by default
        
        firstCondition = False
        secondCondition = False
        
        # While the conditions are false, the loop will continue to iterate.
        
        while not firstCondition or not secondCondition:
            
            # User is prompted to provide an input with a custom message that is created when the method is called.
            
            userInput = str(input(message))
            
            # Conditions are reset depending on what the user inputs.
            # Both conditions are ammended and are assigned True/False values depending on whether the input is 'y' or 'n'
            # The first condition will remain false if the input is not 'y' or 'Y'.
            # The second condition will remain false if the input is not 'n' or 'N'.
            
            firstCondition = userInput in ["y", "Y"]
            secondCondition = userInput in ["n", "N"]
            
            # If statement checks the condition values and returns a true of false value to be used in various areas of the program.
            
            if firstCondition:
                return True
            elif secondCondition:
                return False
            else:
                # If the input is invalid, this message will be displayed e.g., a user enter 'g'.
                
                print("Please enter a valid input.") 
                
    # This method handles string inputs
    
    @staticmethod            
    def prepareForStrInput(message: str):
        error = True
        userInput: str
        
        # Error is assumed and a 'userInput' variable is declared.
    
        while error == True:
            
            # The method attempts to assign the users input the the 'userInput' variable
                
            try:
                userInput = str(input(message))
            
            except:
                # If the value is invalid for whatever reason, this statement will be printed.
                # Strings are quite flexible so it is unlikely this will be called.
                
                print("Please enter a valid input")
                
            # If the user has not inputted anything, they will be prompted to try and enter the input again.
                
            if userInput.__len__() == 0:
                print("No input detected, try again")
                
                continue
            else:
                error = False
                
        # If valid, the user input will be returned.
            
        return userInput

    # Number inputs are handled in this method
    # In some cases, zeros will be needed, and in other cases zeros are not needed.
    # The method assumes that zeros will be allowed, the user can ammend this when the method is called if they don't want zero to be used.

    @staticmethod
    def prepareForNumberInput(message: str, isZeroAllowed: bool = True):
        # An error is assumed be default
        
        error = True
        
        # Value is set already, otherwise an assignment error occurs.
        
        value = 0
        
        # The loop will continue to iterate while the error remains true.
        
        while error == True:
            userInput = input(message)
            
            # This tr
                
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
    
# As there is no registration flow, the user class is set-up to be created with all its attributes already established.

class User:
    id: int
    username: str
    password: str
    
    # This initializes the class, each attribute is set within the class.
    
    def __init__(self):
        # This method is automatically run when the class is instantiated.
        # This values will be set upon creation of the object instance and available in the relevant place.
        
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
            
    def load(self, isItemListPrinted: bool = False):
        self.items.clear()
        
        with open(self.path, "r") as f:
            
            list = f.readlines()
            
            string = ''.join(list)
            
            data = json.loads(string)
            
            for item in data['stock']:
                
                self.addItem(item['name'],
                             item['quantity'],
                             item['price'])
                
            if isItemListPrinted:
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
        
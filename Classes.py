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
            
            # This tries to assign a float value of userInput to the value variable.
                
            try:
                value = float(userInput)
                
            except ValueError:
                # If it is not a number input, a ValueError exception is thrown and the loop iterates.
                
                print("Please enter a number")
                
                continue
            
            # If the value is less than zero (or negative) then a print statement is executed and a user is returned to the beginning of the loop.
            
            if value < 0:
                print("Please enter a positive number")
                
                continue
            
            # This inbedded if is only executed if 'isZeroAllowed' has been set to false.
            # At this point, the method knows that zero inputs are not allowed.
            
            if not isZeroAllowed:
                # Now we are in the statement, if the value happens to be zero, the user will be promted to enter a different value.
                # This involves being taken to the start of the loop.
                
                if value == 0 :
                    print("Please enter a number more than zero")
                
                    continue
                
            # When all the criteria for the input are met, the loop can then be broken.
                
            error = False
            
        # Once the loop is broken, the value the user inputted is returned.
            
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
    
    # This method is called in the relevant area of the program to validate a users login details.
    
    def login(self, username: str, password: str):
        
        # If the username AND password are equal to that of the user instance that has been defined:
        # the user will be able to access the iterations.
        
        if self.user.username == username and self.user.password == password:
            self.isAuthenticated = True
        else:
            # If the credentials don't match, 'isAuthenticated' is set to false, and the value is used in the relevant file.
            # The user will not be able to proceed until this value is True.
            
            self.isAuthenticated = False
            
    # The 'logout' method indicates that the user is no longer authenticated and then ends the program.
            
    def logout(self):
        self.isAuthenticated = False
        
        # This is the last line the program will execute if the user follows the relevant flow.
        # Once this line is executed, the program will end.
        
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
        # All attributes are set appart from the ID, which is set later depending on the items index position in an array.

        self.name = name
        
        # The 'setQuantity' method is used to establish the 'hasStock' attribute as a computed property.
        
        self.setQuantity(quantity)
        self.price = price
        
    def setQuantity(self, value: int):
        # hasStock is set to false if the quantity is set to zero, otherwise it is True.
        
        self.quantity = value
        self.hasStock = value != 0
        
        # hasStock is returned to be used later in another file.
        
        return self.hasStock
        
# The 'ItemStore' class is used to manage items.
# When it is defined, users can create and remove items.
# This updates an array of 'Item(s)' which can then be encoded to JSON.

class ItemStore:
    # Creates an empty array.
    # This can take any instance of any object, but will only be used for 'Item(s)'
    
    items = []
    
    # This grabs the path of the stocklist.txt file.
    
    path = str(pathlib.Path(__file__).parent.resolve() ) + "/Stockpile.txt"
    
    # Once an instance of 'ItemStore' has been established, this method can be utilised.
    # It involves creating an instance of an item usings values established from a users input, appending that item onto the 'items' attribute and then defining its id based on its index position.
    # The item is also returned so it can be used immediately after it is created.
    
    def addItem(self, name, quantity, price):
        
        # An instance of an 'Item' is created
        
        item = Item(name, quantity, price)
        
        # When an item is created, it is appended onto the array of self.items.
        
        self.items.append(item)
        
        # The unique identifier of the item is set using the index position is holds in the self.items array.
        
        item.id = self.items.index(item)
        
        # An item is returned to be used elsewhere if needed.
        
        return item
    
    # This allows for the removal of items when 'ItemStore' has been instantiated.
    # The method takes an index and removes the 'Item' situated at that index.
    
    def removeItem(self, index):
        
        self.items.remove(self.items[index])
        
    # This encodes the array of 'Item(s)' that have been established.
    # This will get called everytime there is an update to the store so the stock list never becomes outdated.
        
    def save(self):
        # stocklist.txt is opened using the path instantiated when an instance of the itemStore is created globally.
        
        with open(self.path, "w") as f:
            
            # Here is where the array of self.items is converted into a JSON format and written into stocklist.txt
            # Each items are converted into python dictionaries using the '.__dict__' inbuilt function using a for loop.
            # This is then held in one more dictionary called 'stock'.
            # 'stock' holds the array of items represented as dictionaries.
            
            f.writelines(str(json.dumps({"stock": [item.__dict__ for item in self.items]}, indent = 2)))
            
    # The load method here is responsible for reading the stockpile.txt file and decoding the JSON in order to access individual elements.
            
    def load(self, isItemListPrinted: bool = False):
        # Before the stocklist is loaded, the array of 'Items' should be cleared each time.
        # The save method will ensure that 'stocklist.txt' us always up to date.
        # Loading the file after '.clear()' has been executed, the 'stocklist.txt' file will be loaded and self.items will have the most recent entries.
        
        self.items.clear()
        
        # Here 'stocklist.txt' is opened with the intention of being read, implicated by "r".
        # The open function will provide different inbuilt methods depending on what character is recieves.
        # We have seen that "w" is write.
        # Other access modes include: "a" for append and "x" for create.
        # Only "r", "x" and "w" are used in this program.
        
        with open(self.path, "r") as f:
            
            # The list variable will contain all the lines of txt present in the txt file, no matter how long it is.
            
            list = f.readlines()
            
            # 'list[str]' is not the format we want for loading the JSON, the JSON needs to be in one string.
            # The 'join()' function "joins" the list of strings together to create one string.
            
            string = ''.join(list)
            
            # Once the string is joined together, it can then be converted from JSON data into dictionaries that python can read.
            # e.g., boolean values are all lowercase in JSON, in python the first letter is uppercase.
            
            data = json.loads(string)
            
            # Now that python can read the list, individual items can be picked out and manipulated.
            
            for item in data['stock']:
                
                # Here is where items are recreated and appended back into the self.items array.
                # Now the program can interact with them as if they were never gone.
                # The save method always ensures this is up to date.
                
                self.addItem(item['name'],
                             item['quantity'],
                             item['price'])
                
            # 'isItemListPrinted' is an extended piece of functionality that prints out the items the JSON has loaded.
            # Whether this is enabled depends on the boolean value is set to true when the method is called.
            # By default it is set to false.
            # In reality, this should have been a seperate method, but it does what it needs to do, and well.
                
            if isItemListPrinted:
                # This print statement indicates to the user the data they are viewing, and infers it is up to date.
                
                print("\nCurrent stock:")
            
                for item in data['stock']:
                    # Like above, we can go through the array of data and pick out the data from 'data' that is relevant to the user.
                    
                    print("\nID: " + str(item['id']))
                    
                    # It is not good for a user to know about an item that is out of stock.
                    # An item knows when it has not quantity.
                    # If the quantity is zero, 'hasStock' will be false and the relevant print statement will be called.
                    
                    if item['hasStock']:
                        print(" Item name: " + item['name'])
                        print(" Item quantity: " + str(int(item['quantity'])))
                        print(" Item price: £" + str(item['price']))
                    else:
                        # Called if an item has a quantity of zero.
                        
                        print(" Item out of stock! Sorry :(")
                        
    # This method handles the purchase of an item.
                
    def buyItem(self, id, quantity: int):
        
        # The moment the method is called we know the user is buying an item.
        # 'isBuyingItem' indicates a user is buying an item.
        
        isBuyingItem = True
        
        # The items is found using an ID the user has showed interest in and inputted earlier.
        # This will never be out of range as a try/except statement handles this in iteration 2.
        
        item: Item = self.items[id]
        
        while isBuyingItem:
            
            # Here we are taking the quantity the user has requested and subtracting it from the quantity of that item held in the stocklist.

            item.quantity -= quantity
            
            # This value is the reassigned to the item quantity through the 'setQuantity' method.
            # This is so the 'hasStock' attribute is updated to reflect whether there is any stock of the item left or not.
            
            item.setQuantity(item.quantity)
            
            # We know once the quantity has been subtracted from the relevant item in the stocklist that the transaction must be complete.
            # The loop can be exited by setting 'isBuyingItem' to false.
            
            isBuyingItem = False
            
        # It is important that once the item is purchased that the 'stocklist.txt' file is updated.
        # The if statement ensures that the purchase has definately been confirmed.
        # It is impossible at this stage that this value would not be false, unless there is something I have missed.
        # I have decided to include it anyway.
            
        if not isBuyingItem:
            self.save()
            
# This is the instace of itemStore that is referenced throughout the app.
# There is to only ever be one instance so that all the data correlates thoughout the program.
    
itemStore = ItemStore()
        
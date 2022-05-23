from textwrap import indent
from xml.dom.expatbuilder import Rejecter
import Classes
import logging
import pathlib

# read = "r"
# append = "a"
# write = "w"
# create = "x"
# text = "t"
# binary = "b"

itemStore = Classes.ItemStore()
    
def prepareToContinue():
    
    firstCondition = False
    secondCondition = False
    
    while not firstCondition or not secondCondition:
        
        userInput = str(input("Please enter y/n: "))
        
        firstCondition = userInput in ["y", "Y"]
        secondCondition =  userInput in ["n", "N"]
        
        if firstCondition:
            return True
        elif secondCondition:
            return False
        else:
            print("Please enter a valid input.")
            
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

def prepareForNumberInput(message: str):
    error = True
    userInput: float
    
    while error == True:
            
        try:
            userInput = input(message)
            
        except:
            print("Please enter a valid input")
            
        error = False
        
    return userInput

    
def add():
    global itemStore
    
    isAdding = True

    while isAdding == True:
        
        nameInput = prepareForStrInput("Please enter what item you wish to add: ")
        quantityInput = int(prepareForNumberInput("How many items are you adding?: "))
        priceInput = prepareForNumberInput("How much does this item cost?: ")

        item = itemStore.addItem(nameInput, 
                                    quantityInput, 
                                    priceInput)
        
        itemStore.save()
    
        isAdding = prepareToContinue()

def start():
    
    try:
        open(itemStore.path, "x")
    except:
        
        print("Loaded stocklist")
        
        try:
            itemStore.load()
        except:
            print("No data found")
        
        
    
    add()
    
start()


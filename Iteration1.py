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
        
        firstCondition = userInput in ["y", "Y"] or userInput is 'yes'
        secondCondition =  userInput in ["n", "N"] or userInput is 'no'
        
        if firstCondition:
            return True
        elif secondCondition:
            return False
        else:
            print("Please enter a valid input.")
            
def prepareForStrInput(message):
    error = True
    
    while error == True:
            
        try:
            input = str(input(message))
            
            if input.__len__() == 0:
                print("No input detected, try again")
                
                error = True
                
        except:
            print("Please enter a valid input")
            
            error = True
            
    return input

def prepareForIntInput(message):
    error = True
    
    while error == True:
            
        try:
            input = int(input(message))
            
            if input.__len__() == 0:
                print("No input detected, try again")
                
                error = True
                
        except:
            print("Please enter a valid input")
            
            error = True
            
    return input

    
def add():
    global itemStore
    
    isAdding = True

    with open(str(str(itemStore.path) + "Stockpile.txt"), "w") as f:
        while isAdding == True:
            
            nameInput = str(input("What item would you like to add?: "))
            quantityInput = int(input("How many items are you adding?: "))
            priceInput = float(input("How much does this item cost?: "))
    
            item = itemStore.addItem(nameInput, 
                                     quantityInput, 
                                     priceInput)
            
            itemStore.save()
        
            isAdding = prepareToContinue()

def start():
    
    try:
        open(str(str(itemStore.path) + "Stockpile.txt"), "x")
    except:
        itemStore.load()
        
        print("Loaded stocklist")
    
    add()
    
start()


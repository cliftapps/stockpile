# Here I have imported Classes that holds all the reusable elements that are used throughout every file.
# Iteration 1 and 2 are also imported to the relevant flows can be started.

# NOTE: Some strings will be seperated into seperate variables to improve screenshot visibility.

import Classes
import Iteration1
import Iteration2

# This reduces the amount of text that will be present in this file.
# The methods within Classes.Inputs are static so the instantiation of an object is not needed.

inputs = Classes.Inputs

def login():
    # Python required a reference to global variables within methods.
    
    global inputs
    
    # Instance of security class is created.
    security = Classes.Security()

    # Loop continues while the user is not authenticated.
    # Look will not be broken until user is authenticated.
    while not security.isAuthenticated:
        # Prints screen title.
        
        print("\n--Login--")
        if not security.isAuthenticated:
            # User must input both details before authentication occurs, this improves security as the user won't know which credential they got wrong.
            
            username = str(input("\nPlease enter your username: "))
            password = str(input("Please enter your password: "))
            
            # Code in login function validates whether user has entered the correct combination of details or not.
            
            security.login(username, password)
        
        # When a user is authenticated (have entered the right usernamed and password to satisfy the criteria of the login function),
        # they will be authenticated.
        
        if security.isAuthenticated:
            
            # This loop indicates the current login session, allowing a user to choose whether they want to view/order stock or,
            # to insert stock.
            
            iterationChoiceMessage = "\nPlease enter 'i' to insert stock, or 'v' or 'o' to view/order stock: "
            
            while security.isAuthenticated:
                if inputs.prepareToContinue(iterationChoiceMessage, 
                                            isIterationDecision = True):
                    # This calls the method start() from within Iteration 1 which starts the stock insertion flow.
                    
                    Iteration1.start()
                else:
                    # This calls the method start() from within Iteration 2 which starts the view/order stock flow.
                    
                    Iteration2.start()
                    
                # Once a user has finished with either iteration 1 or 2, they will be asked whether they want to continue their session or end the session.
                
                message = "Would you like to remain logged in? y/n: "   
                    
                if inputs.prepareToContinue(message):
                    continue
                else: 
                    break
        else:
            # If a user enters invalid details, this message will be displayed.
            
            print("Invalid login, please enter the correct username or password!")
            
    # If a user has indicated they no longer want to remain logged in, security.logout will be performed.
    # Within this method, the final lines of code are run so the program will end after the method has completed.
    # The users is also no longer authenticated when this script is run, although this has no effect on the current functionality.
            
    security.logout()
    
# This calls the login function which leads to the rest of the program flow.
            
login()
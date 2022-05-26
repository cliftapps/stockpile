import Classes
import Iteration1
import Iteration2

# This reduces the amount of text that will be present in this file.
# The methods within Classes.Inputs are static so the instantiation of an object is not needed.

inputs = Classes.Inputs

def login():
    # Python required a reference to global variables within methods.
    
    global inputs
    
    security = Classes.Security()

    while not security.isAuthenticated:
        print("\n--Login--")
        if not security.isAuthenticated:
            username = str(input("Please enter your username: "))
            password = str(input("Please enter your password: "))
            
            security.login(username, password)
        
        if security.isAuthenticated:
            while security.isAuthenticated:
                if inputs.prepareToContinue("\nPlease enter 'y' to insert stock or 'n' to order stock: "):
                    Iteration1.start()
                else:
                    Iteration2.start()
                    
                if inputs.prepareToContinue("Would you like to remain logged in? y/n: "):
                    continue
                else: 
                    break
        else:
            print("Invalid login, please enter the correct username or password!")
            
    security.logout()
            
login()
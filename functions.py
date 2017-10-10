# This is the file where you can add your custom functions.
# You can also split functions into their own files, but
# remember to add that to the menu.py file
# eg. from mynewfile import mynewfunc
import os.path

# never remove this validator
# validates user-input concerning options in the menu
def number_validator(value1):

    options_list = [1,2,3,99] # current set of options in menu.py
    # [REMEBER TO ADD YOUR NEW OPTION TO THE OPTIONS_LIST ABOVE]

    if value1.isdigit():
        value2 = int(value1) # This line converts the user-provided option into an integer

        if value2 in options_list:
            return value2 

        # If the value is an integer but not present in options_list
        else:
            print("\n******************************************")
            print("Option Invalid! Going back to main menu...")
            print("******************************************\n")

            return 0

    # If the value is not an integer
    else:
        print("\n**************************************************")
        print("Error! Incorrect input! Going back to main menu...")
        print("**************************************************\n")

        return 0
        
# print from function
def print_me():

    print("\n***************")
    print("I am print_me()")
    print("***************\n")
    
# adding 2 numbers together
def add_two(val1, val2):
    
    if val1.isdigit() and val2.isdigit():
    
        val1_int = int(val1)
        val2_int = int(val2)
    
        total = val1_int + val2_int
    
        print("\n**************")
        print("I am add_two()")
        print("**************\n")
        
        print(val1 + " + " + val2 + " =")
        print(total)
        
    else:
        print("\n**************************************************")
        print("Error! Incorrect input! Going back to main menu...")
        print("**************************************************\n")
        
# [ADD YOUR FUNCTION BELOW]
# do_something()

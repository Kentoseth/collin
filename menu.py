# This is a template of Collin
# [ALL INSTRUCTIONS SHOWN LIKE THIS ARE MEANT FOR YOUR BENEFIT]

import sys
import os
# [ADD YOUR NEW FUNCTIONS AFTER import BELOW]
from functions import number_validator, print_me, add_two

holder = 0 # this variable is for holding application state

print("\n*****************")
print("Welcome to Collin")
print("*****************\n")

while holder == 0:

    print("Please select an option:\n")
    print("1: Option 1\n")
    print("2: Option 2\n")
    print("3: Option 3\n")
    # print("[ADD YOUR OPTION TITLE HERE]\n")
    print("99: Exit app\n")
    
    
    holder_input = input("Your input: ") # This input variable stores the option the user selects

    holder = number_validator(holder_input) # Validating the user input

    if holder == 1:
        
        print("\n************")
        print("Hello World!")
        print("************\n")
        
        holder = 0 # never remove, always add to the end of each if/elif

    elif holder == 2:

        print_me() # call to external function from functions.py

        holder = 0 # never remove, always add to the end of each if/elif

    elif holder == 3:
        
        int1 = input("Please enter first integer: ")
        
        int2 = input("Please enter second integer: ")

        add_two(int1, int2) # passing local input to external function
        
        print("\n") # added padding

        holder = 0 # never remove, always add to the end of each if/elif
        
    
    # [ADD YOUR NEW OPTION BELOW - PLACEHOLDER PROVIDED]
    # elif holder == 4:
    #    do_something()
    #    holder = 0
    

    # Never delete this exit option
    elif holder == 99:
        print("\n GOODBYE!!! \n")

        sys.exit()

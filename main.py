from colorama import *
import sys
import time
import os

def cool_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.010)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

        
def make():
    cls()
    cool_print(f"""
______________________
{Fore.WHITE}-->{Fore.RESET} 1. {Fore.GREEN}First Option{Fore.RESET}
{Fore.WHITE}-->{Fore.RESET} 2. {Fore.GREEN}Second Option{Fore.RESET}
{Fore.WHITE}-->{Fore.RESET} 3. {Fore.GREEN}Third Option{Fore.RESET}
______________________
Please type a selection number: """)
    global response
    response = input("")
    if int(response) == 1:
       first_function()
    elif int(response) == 2:
        second_function()
    elif int(response) == 3:
         third_function()
    

def first_function():
    cls()
    print("You choosed the first option!")
    print("Press enter to go back to the menu.")
    input()
    make()
def second_function():
    cls()
    print("You choosed the second option!")
    print("Press enter to go back to the menu.")
    input()
    make()
def third_function():
    cls()
    print("You choosed the third option!")
    print("Press enter to go back to the menu.")
    input()
    make()
    
make()

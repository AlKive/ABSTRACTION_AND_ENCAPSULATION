# BABIERA,ALEXA | CMPE-103-MODULE-6-ABSTRACTION AND ENCAPSULATION|
# ASSIGNMENT #9 (PROGRAMMING EXERCISE 20)
from colorama import Back, Fore, Style, init
from tkinter import *
from tkinter import simpledialog
ws=Tk()
#import PET class
from PetClass import PET
#user input prompts
pet_name = simpledialog.askstring("PET'S NAME", "Enter your pet's name : ", parent= ws)
pet_type = simpledialog.askstring("ANIMAL TYPE", "Enter your pet's animal type: ", parent= ws) 
pet_age = simpledialog.askinteger("PET'S AGE", "Enter your pet's age : ", parent= ws)

#create PET object
PET_INFO = PET(pet_name, pet_type, pet_age)
#display output
PET_INFO.display()

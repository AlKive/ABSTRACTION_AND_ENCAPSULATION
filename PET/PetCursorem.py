# BABIERA,ALEXA | CMPE-103-MODULE-6-ABSTRACTION AND ENCAPSULATION|
# ASSIGNMENT #9 (PROGRAMMING EXERCISE 20)
#import PET class
from PetClass import PET
#user input prompts
pet_name = input("Enter your pet's name : ")
pet_type = input("Enter your pet's animal type: ") 
pet_age = input("Enter your pet's age : ")

#create PET object
PET_INFO = PET(pet_name, pet_type, pet_age)
#display output
PET_INFO.display()

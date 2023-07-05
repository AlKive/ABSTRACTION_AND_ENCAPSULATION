# BABIERA,ALEXA | CMPE-103-MODULE-6-ABSTRACTION AND ENCAPSULATION|
# ASSIGNMENT #9 (PROGRAMMING EXERCISE 20)

from colorama import Back, Fore, Style, init
from tkinter import *
from tkinter import messagebox

#create class
class PET:
    def __init__(self, name, animal_type, age):
        # instance variables
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
#create methods
   #setters
    def set_name(self, name):
            self.__name = name

    def set_type(self, animal_type):
            self.__animal_type = animal_type

    def set_age(self, age):
            self.__age = age
            
    #getters
    def get_name(self):
            return self.__name
        
        # get animal type
    def get_type(self):
            return self.__animal_type
        
        # get age
    def get_age(self):
            return self.__age
    #display
    
    def display(self):
        messagebox.showinfo("Pet's Name :", self.__name)
        messagebox.showinfo("Animal Type :" , self.__animal_type)
        messagebox.showinfo("Pet's Age :" , self.__age)


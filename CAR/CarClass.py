# BABIERA,ALEXA | CMPE-103-MODULE-6-ABSTRACTION AND ENCAPSULATION|
# ASSIGNMENT #9 (PROGRAMMING EXERCISE 19)
from colorama import Back, Fore, Style, init
import time
from tkinter import *
# Create Car class
class CAR:
# init/create constructor
    def __init__ (self, year_model = 2020, make = "Chevrolet Corvette", speed=0):
        self.__year_model = year_model 
        self.__make = make
        self.__speed = speed
#Create method for car's acceleration (+5 speed) and brake (-5) whenever called
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5        
#get car's speed
    def current_speed(self):
        return self.__speed
#display the car's speed
    def accelerating_speed_display(self):
        print(Fore.GREEN + " Speed: ",Fore.WHITE + str(self.__speed), Fore.YELLOW + "kph")
    def brake_speed_display(self):
        print(Fore.MAGENTA + " Speed: ",Fore.WHITE + str(self.__speed), Fore.YELLOW + "kph")
 
    def separator_display (self):
        time.sleep(2)
        print (Fore.LIGHTWHITE_EX + "︶꒦꒷♡꒷꒦︶"* 7)

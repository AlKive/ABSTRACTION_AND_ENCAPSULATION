#import class FAN
from FanClass import FAN
from colorama import Back, Fore, Style, init
import time
from tkinter import *
from termcolor import colored
import pyfiglet

#create function for FAN 1
def FAN1_RUN ():
# create object
  FAN1 = FAN()  
# display object's attributes
#Object 1 Attributes
  FAN1.set_speed(3)
  FAN1.set_radius(10)
  FAN1.set_color('Yellow')
  FAN1.set_status(True)
  FAN1.fan1_attributes()
  
def Kemerut():
        text = "FAN 1 ATTRIBUTES : "
        font = "digital"
        color = "yellow"
        output = pyfiglet.figlet_format(text, font=font, width=200)
        outputColor = colored(output, color)

        time.sleep(2)
        print(Fore.YELLOW + "=" * 96)
        time.sleep(2)
        print("🌼" * 48)
        for line in outputColor.split("\n"):
            print(line.center(90))
        print("🌼" *48 )  
        
def Kemerut2():
        text = "FAN 2 ATTRIBUTES : "
        font = "digital"
        color = "yellow"
        output = pyfiglet.figlet_format(text, font=font, width=200)
        outputColor = colored(output, color)

        time.sleep(2)
        print(Fore.YELLOW + "=" * 96)
        time.sleep(2)
        print( "🌸" * 48)
        for line in outputColor.split("\n"):
            print(line.center(90))
        print("🌸" *48 )          
  
def FAN2_RUN ():
# create objects
  FAN2 = FAN()
# display object's properties
#Object 2 Attributes
  FAN2.set_speed(2)
  FAN2.set_radius(5)
  FAN2.set_color('Blue')
  FAN2.set_status(False)
  FAN2.fan2_attributes()  
  
Kemerut()  
FAN1_RUN()
Kemerut2()
FAN2_RUN()
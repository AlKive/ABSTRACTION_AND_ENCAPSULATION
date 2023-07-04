'''PSEUDOCODE'''
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
def display_current_speed(self):
 print(" Speed: ",self.__speed,"kph")

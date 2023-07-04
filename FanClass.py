#create fan class
class FAN:
    def __init__ (self, speed = 'SLOW', radius = 5, color = 'Blue', status = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__status = status
        
# define methods
# create private int data for speed
    def set_speed(self,speed):
        self.__speed = speed
# create private bool data for power(ON/OFF)
    def set_status(self, status):
        self.__status = bool(status)
 
        
# create private float data for radius        
    def set_radius(self, radius):
        self.__radius = float(radius)
        
# create private string data for color
    def set_color(self, color):
        self.__color = str(color) 
        
# create getters
    def get_speed(self):
        return self.__speed

    def get_status(self):
        return self.__status

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color
    
    #Display
    def fan1_attributes(self):
        print("SPEED: ", self.__speed, "\nRADIUS: ", self.__radius, "\nCOLOR: ", self.__color, "\nPOWER: ", self.__status, "\n")
    def fan2_attributes(self):
        print("SPEED: ", self.__speed, "\nRADIUS: ", self.__radius, "\nCOLOR: ", self.__color, "\nPOWER: ", self.__status, "\n")        
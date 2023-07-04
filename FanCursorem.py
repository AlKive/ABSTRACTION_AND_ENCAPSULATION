#import class FAN
from FanClass import FAN

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

def FAN2_RUN ():
# create objects
  FAN2 = FAN()
'''Pseudocode'''
#import car class
from CarClass import CAR
#create object for car
Chevrolette = CAR()
# call the accelerate method five times and display current speed (using FOR-LOOP)
for i in range (5):
    Chevrolette.accelerate()
    Chevrolette.accelerating_speed_display()

Chevrolette.separator_display()
    
# call brake method five times and display current speed (USING FOR-LOOP)
for i in range (5):
    Chevrolette.brake()
    Chevrolette.brake_speed_display()



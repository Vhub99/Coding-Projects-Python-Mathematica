# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:37:55 2020

@author: User
"""

import math

#Inputs
target = int(input("Enter distance of target (m): "))
yo = int(input("Enter Archer's height (m): "))
dt = float(input("Enter desired time step (s): "))
com = "Y"
while com == "Y":
    xo = 0
    vo = float(input("Enter initial launch velocity (m/s): "))  # Initial launch velocity
    to = int(input("Enter intial launch angle (degrees): "))  # Launch angle
    g = 9.81  # Gravitational Constant
    vxo = vo * math.cos(math.radians(to))  #Intial X velocity
    vyo = vo * math.sin(math.radians(to))
    
    #Calculations
    # The code works by finding a value that's 0.5m away from the specified range
    minr = target - 0.5
    maxr = target + 0.5
    xf = 0
    t = 0
    yc = yo + vyo * dt - (1 / 2) * g * dt**2
    while yc > 0:
      yc = yc + vyo * dt - ((1 / 2) * g * t**2)
      t = t + dt
    tf = t
    yf = yc
    xf = xo + vxo * tf
    if xf < minr:
        c = minr - xf
        print("You are ", round(c,1),
              " meters away from target. Increase launch velocity")
        com = input("Reshoot arrow? Y or N: ")
    elif xf > maxr:
        c = xf - maxr
        print("You are ", round(c,1),
              " meters away from target. Decrease launch velocity")
        com = input("Reshoot arrow? Y or N: ")
    else:
        print("You hit the target!")
        com = "N"

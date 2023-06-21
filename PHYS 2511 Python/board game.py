# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:04:15 2020

@author: vicky
"""
import random
random.randint(1,6) 
y = list(range(100))
print("Welcome!")
p1 = 0
p2 = 0
def roll_dice():
    return r
while 1:
    r = random.randint(1,6)
    if r == 1: 
        p1 = p1 + 1
        p2 = p2 + 1
        print("Move 1 space")
    if r == 2:
        p1 = p1 + 2
        p2 = p2 + 2
        print("Move 2 spaces")
    if r == 3:
        p1 = p1 + 3
        p2 = p2 + 3
        print("Move 3 spaces")
    if r == 4:
        p1 = p1 + 4
        p2 = p2 + 4
        print("Move 4 spaces")
    if r == 5:
        p1 = p1 + 5
        p2 = p2 + 5
        print("Move 5 spaces")
    if r == 6:
        p1 = p1 + 6
        p2 = p2 + 6
        print("Move 6 spaces")
    moveback = [20, 27, 54, 76, 87]
    moveforward = [5, 29, 56, 80, 90]
    moveback2 = [3, 30, 67, 83, 93]
    moveforward2 = [7, 33, 42, 79, 82]
    stay = [10, 38, 63, 84, 91]
    if p1 in moveback:
        p1 = -5
        print("move back")
    if p2 in moveback:
        p2 = -5
        print("move back")
    if p1 in moveback2:
        p1 = -10
        print("move back")
    if p2 in moveback2:
        p2 = -10
        print("move back")
    if p1 in moveforward:
        p1 = +5
        print("move forward")
    if p2 in moveforward:
        p2 = +5
        print("move forward")
    if p1 in moveforward2:
        p1 = +80
        print("move forward")
    if p2 in moveforward2:
        p2 = +80
        print("move forward")
    if p1 in stay:
        p1 = 0
    if p2 in stay:
        p2 = 0
    print(p1, p2)
    if p1 > 101:
        print("p1 wins")
        break 
    if p2 > 101:
        print("p2 wins")
        break 


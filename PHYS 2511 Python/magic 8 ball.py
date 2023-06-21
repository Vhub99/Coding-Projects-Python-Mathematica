# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:54:04 2020

@author: vicky
"""
import random
random.randint(0,1)
import time
while 1:
    x = input("your name?")
    if type(x) == type("str"):
        print("thanks! and wlecome")
        break
r = random.randint(0,1)
print("ask me a question!")
if r == 0:
    answer = "yes"
if r == 1:
    answer = "no"
question = input()
print("thinking...")
time.sleep(0.5)
print(question, answer)
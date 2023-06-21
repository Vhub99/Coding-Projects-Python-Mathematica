# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:06:48 2020

@author: vicky
"""
import numpy as np
import scipy.integrate as sit
import matplotlib.pyplot as plt

print("Enter delta x")
dx = float(input())
a = -5.0
b = 5.0
n = 1.0

N = int(float(((b-a)/int(float(dx))+n)))
x, trash = np.linspace(a,b,N, endpoint=False, retstep=True)
print(type(x))

def func1(x):
    return -0.5*(x) + 4.0
def func2(x):
    return -0.29*x**2 - x + 12.5
def func3(x):
    return 1.0 + 10*(x + 1.0)*np.exp(-x**2)


y1 = func1(x) 
y2 = func2(x)
y3 = func3(x) 

plt.figure(figsize=(15,5))

plt.subplot(1,3,2)
plt.plot(x,y1,'b')
x_mid = (x[:-1] + x[1:])/2 # Midpoints
y_mid = func1(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.4,edgecolor='b')
plt.title('Riemann Sum for A, N = {}'.format(N))

plt.show()
A = sit.quadrature(func1, -5.0, 5.0)
print(A)

plt.figure(figsize=(15,5))

plt.subplot(1,3,2)
plt.plot(x,func2(x),"b")
riemannx = (x[:-1] + x[1:])/2
riemanny = func2(riemannx)
plt.plot(riemannx,riemanny,"b",markersize=10)
plt.bar(riemannx,riemanny,width=dx,alpha=0.2,facecolor='b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Riemann Left Sum for B')
plt.xlim(-5,5)
plt.ylim(0,20)
plt.show()

B = sit.quadrature(func2, -5.0, 5.0)
print(B)

plt.figure(figsize=(15,5))

plt.subplot(1,3,3)
plt.plot(x,func3(x),"b")
riemannx = (x[:-1] + x[1:])/2
riemanny = func3(riemannx)
plt.plot(riemannx,riemanny,"b",markersize=10)
plt.bar(riemannx,riemanny,width=dx,alpha=0.2,facecolor='b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Riemann Left Sum for C')
plt.xlim(-5,5)
plt.ylim(0,20)
plt.show()

C = sit.quadrature(func3, -5.0, 5.0)
print(C)










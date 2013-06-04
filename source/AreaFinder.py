#-------------------------------------------------------------------------------
# Name:        Area Finder
# Purpose:     Find useful info
# Author:      steve.stiles
# Created:     07/11/2012
# Copyright:   (c) steve.stiles 2012
#-------------------------------------------------------------------------------

#Intro Text
import math
print()
print("Welcome to Area Finder")
print("By Mix Masta DJ Stylin' Steve Stiles")
print()

#Global Variables
shape = input("What's your shape? ")
u = input("What are your units? ")

#Define Shapes Here
#Cylinders
def cylinder():
    r = float(input("What's your radius? "))
    h = float(input("What's your height? "))

    print("Area of your Cylinder: ")
    print(2*(math.pi)*r**2 + h*2*math.pi*r)
    print("cubic %s" %u)

#Circles
def circle():
    r = float(input("What's your radius? "))
    print("Area of your Circle: ")
    print(math.pi*r**2)
    print("square %s" %u)

#Spheres
def sphere():
    r = float(input("What's your radius? "))
    print("Area of your Sphere: ")
    print(math.pi*r**3*(4/3))
    print("cubic %s" %u)

#Rectangles
def rectangle():
    b = float(input("What's your base? "))
    h = float(input("What's your height? "))
    print("Area of your rectangle: ")
    print(b*h)
    print("square %s" %u)

#Triangles
def triangle():
    b = float(input("What's your base? "))
    h = float(input("What's your height? "))
    print("Area of your triangle: ")
    print((0.5*b)*h)
    print("square %s" %u)


#Start Conditionals Here
if shape == "cylinder":
    cylinder()
elif shape == "Cylinder":
    cylinder()

if shape == "circle":
    circle()
elif shape == "Circle":
    circle()

if shape == "sphere":
    sphere()
elif shape == "Sphere":
    sphere()

if shape == "rectangle":
    rectangle()
elif shape == "Rectangle":
    rectangle()

if shape == "triangle":
    triangle()
elif shape == "Triangle:":
    triangle()
#!/usr/bin/env python3

import math 

class Planet:
    def __init__(self):
        print("I AM CREATED!")
    def density(self):
        pass

# self is a minimum argument
# __init__ is not mandatory, but it solves a lot of inefficiency later
# A function inside a class is called a method

planet1 = Planet()
planet1.name = "Mercury"
planet1.mass = 1
planet1.radius = 1
print(planet1.density)

# Now we are going to utilize __init__
# self. variables in __init__ are global in class scope
# U don't need to specify arguments in another method

class Planet:
    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass
        self.radius = radius
        print(f"{self.name} has been created!")
    def density(self):
    	return self.mass/(4/3*math.pi*math.pow(self.radius,3))

planet2 = Planet("Mercury", 1, 1)
print(planet2.density())

# Calling attribute and method
print(planet2.name)
print(planet2.density())

# Default value and data types

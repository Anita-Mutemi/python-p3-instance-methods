#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    def bark(self):
        print("Woof!")
    def sit(self):
        print("The dog is sitting.")

fido = Dog()
fido.bark()
fido.sit()
#we create those objects by calling our class just as we would a function in closed paranthesis
#<__main__.Dog object at 0x1027f07f0>
# python3 lib/dog.py
# Woof!
# passed 3 tests to this point
#create a second instance

snoopy = Dog()
snoopy.bark()
snoopy.sit()

#add an instance of sit

# ['__module__', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__',
# '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__',
# '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__new__',
# '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__',
# '__format__', '__sizeof__', '__dir__', '__class__']

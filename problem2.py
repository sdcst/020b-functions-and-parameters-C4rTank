#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math



def distance():
    a = False
    while a == False:
        x = input("Please input an x value: ")
        try:
            x = float(x)
            a = True
            b = False
        except:
            print("Invalid input")
            print("Please try again")

    while b == False:
        y = input("Please input an y value: ")
        try:
            y = float(y)
            b = True
        except:
            print("Invalid input")
            print("Please try again")
    if x > y:
        d = x - y
    elif x < y:
        d = y - x

    print('The distance between' ,x, 'and' ,y, 'is', d)

distance()
#done
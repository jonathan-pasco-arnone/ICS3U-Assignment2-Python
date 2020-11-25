#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: November 2020
# This program calculates the volume of a sphere

import math


def main():
    # This function gets the volume of the sphere and outputs it

    radius_Str = input("What is the radius of this sphere: ")
    radius = int(radius_Str)
    volume = 4/3 * math.pi * math.pow(radius, 3)
    print("If the radius of the sphere is " + radius_Str + "mm")
    print("Then the volume is {:.2f}mm³".format(volume))


if __name__ == "__main__":
    main()

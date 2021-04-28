#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on April 2021
# This program calculates the circumference of a circle
#       with dimensions inputted from the user

import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter the radius of the circle (mm):"))

    # process
    circumference = constants.TAU * radius

    # output
    print("Circumference is {} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()

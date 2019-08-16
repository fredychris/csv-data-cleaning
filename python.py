#!/usr/bin/python3
import os
import sys

def myfunction(all):
    print("Welcome\n")
    print("EURON BANK ENTERPRISES\n")

    password = '1234'

    input(password)

    if password != '1234':
        print("Wrong password")

    else:
        print("Euron BANK\n")


if __name__ == "__main__":

    print("ENTER YOUR PASSWORD\t")

    input(password)

    print("\n")

    myfunction(all)
    
print("Allow access")
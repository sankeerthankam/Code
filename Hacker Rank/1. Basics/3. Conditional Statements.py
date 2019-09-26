# Task:
# Given an integer, perform the following conditional actions:
# If odd, print Weird
# If even and in the inclusive range of to 2 and 6, print Not Weird
# If even and in the inclusive range of to 7 and 20, print Weird
# If is even and greater than 20, print Not Weird

#!/bin/python3

import math
import os
import random
import re
import sys

def weird(num):
    if num % 2 != 0:
        print('Weird')
    else:
        if num >= 2 and num <= 5:
            print("Not Weird")
        if num >= 6 and num <= 20:
            print("Weird")
        elif num > 20:
            print("Not Weird")


if __name__ == '__main__':
    N = int(input())
    weird(N)

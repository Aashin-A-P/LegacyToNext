#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    day = 13
    
    if (year < 1918):
        if (year % 4 == 0):
            day -= 1;
    
    
    elif (year == 1918):
        day += 13
    
    else:
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            day -= 1
    
    return str(day) + ".09." + str(year)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

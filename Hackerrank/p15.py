'''You are aked to ensure that the first and last names of people begin with a capital letter in thier passports.
For example, alison heck should be capitalized correctly as Alison Heck.'''

#!/bin/python3

import math
import os
import random
import re
import sys

# complete the solve function below.
def solve(s):
    s2 = ' '.join(word.capitalize() for word in s.split(' '))
    return s2
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'],'w')
    s = input()
    result = solve(s)
    print(result)
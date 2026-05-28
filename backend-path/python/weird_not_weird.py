#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N % 2 != 0:
        print("Weird")
    for (i in range(2, 5)):
        if N % 2 == 0:
            print("Not Weird");

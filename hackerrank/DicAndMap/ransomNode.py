import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):    
    #Use counter to turn a list to a dict faster
    m = Counter(magazine)
    n = Counter(note)
    for key,value in n.items():
        if key in m and m.get(key) >= value:
            continue 
        else:
            print("No")            
            return
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)


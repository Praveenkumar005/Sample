import math
import os
import random
import re
import sys

n=int(input())
if n%2!=0:
    print("Weird")

elif n%2==0:
     if n in range(2,6):
#if we want range between 2 to 5 means we put range from 2 to 6. Because last number in range is not taken.
      print("Not Weird")
     elif n in range(6,21):
      print("Weird")
     elif n>20:
      print("Not Weird")
else:
   print("Weird")  
    
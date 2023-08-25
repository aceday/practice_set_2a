import os
from math import sqrt
def heron_perimtr(a,b,c)->float:
    s=(a+b+c)/2
    return s
def heron_area(h,a,b,c):
    a=sqrt(h*(h-a)*(h-b)*(h-c))
    return a
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.name == 'clear'
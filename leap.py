# <202280005@psu.palawan.edu.ph>
# Function 1: Calculate Weighted Average
# Coder: Mark Cedie Buday @ BSCS2-B1
# Schedule01: T: 11:00-13:00 CE Bldg 15
# Schedule02: F: 10:00-13:00 NIT 1
# Date Created: 2023-08-24

from os import *
def cls():
  if name == 'nt':
    system('cls')
  else:
    system('clear')
    
def leap_year(y):
  if (y%400==0) and (y%100==0):
    return f"{y} is a leap year"
  elif (y%4==0) and (y%100!=0):
    return f"{y} is a leap year"
  else:
    return f"{y} is not a leap year"

cls()
try:
  leap_yr = int(input('\n:: Enter year: '))
  print(leap_year(leap_yr))
except ValueError:
  print('[!] Enter the year again!')
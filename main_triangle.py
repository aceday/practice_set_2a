# <202280005@psu.palawan.edu.ph>
# Function 1: Calculate Weighted Average
# Coder: Mark Cedie Buday @ BSCS2-B1
# Schedule01: T: 11:00-13:00 CE Bldg 15
# Schedule02: F: 10:00-13:00 NIT 1
# Date Created: 2023-08-24

from triangle import *
cls()
unit='cm'
try:
    x = float(input('\n:: Enter 1st value: '))
    y = float(input(':: Enter 2nd value: '))
    z = float(input(':: Enter 3rd value: '))
    hp = heron_perimtr(x,y,z)
    ha = heron_area(hp,x,y,z)
    print(f'\nS = ({x})+({y})+({z})/2 = {hp}{unit}')
    print(f'\n[∆XYZ = {ha:.2f}{unit}]')
except ValueError:
    print('\n[!] Enter the value again!')
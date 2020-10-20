#to clear screen at the beginning of the program so it looks nice
import os
os.system('cls')
#to get a more accurate value for pi, stretch challenge 1
import math

square_length=float(input('\nWhat is the length of a side of a square in centimeters? '))
#added new line so program is easier to read.
print(f'The area of the square is: {square_length**2} square centimeters or {(square_length**2)/10000} square meters')

rectangle_length=float(input('\nWhat is the length of the rectangle in centimeters? '))
rectangle_width=float(input('What is the width of the rectangle in centimeters? '))
print(f'The area of the rectangle is: {rectangle_length*rectangle_width} square centimeters or {rectangle_length*rectangle_width/10000} square meters')

radius=float(input('\nWhat is the radius of the circle in centimeters? '))
print(f'The area of the circle is: {math.pi*(radius**2)} square centimeters or {math.pi*(radius**2)/10000} square meters\n')
#alternative way to calculate
#area_of_circle=3.14*(radius**2)
#print(f'The area of the circle is: {area_of_circle}')

#stretch challenge 2
length_value=float(input('What is your length value? '))
print(f'The area of a square with that length of side is: {length_value**2}')
print(f'The area of a circle with that radius is: {math.pi*length_value**2}')
print(f'The volume of a cube with that length of side is: {length_value**3} ')
print(f'The volume of a sphere with that radius is: {4/3*math.pi*length_value**3}\n')


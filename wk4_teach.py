import os
os.system('cls')
import math

print('Welcome to the velocity calculator. Please enter the following: \n')

m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
c = (1/2) * p * A * C
print(f'\nThe inner value of c is: {c:.3f}')
velocity_at_t = math.sqrt(m * g / c) * (1 - math.exp((- math.sqrt(m * g * c) / m) * t))
print(f'The velocity after {t} seconds is {velocity_at_t:.3f} m/s.\n')

print('Lets determine the terminal velocity of a 7 kg bowling ball with a radius of 0.108 meters.\n')

g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = math.pi * 0.108**2 
C = 0.5
c = (1/2) * p * A * C
v_terminal = math.sqrt(7 * g / c)
print(f'The terminal velocity is {v_terminal:.3f} m/s.')


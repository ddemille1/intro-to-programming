# import os to clear the screen later
import os
import sys

#putting the whole program into a function. function will be called when invalid resonse so program will restart.
def script():

#clearing screen
    os.system('cls')

#defining the functions that will be used
    def convert_to_f(celsius):
        converted_to_f = celsius * (9/5) + 32
        return converted_to_f

    def find_wind_chill(temp, velocity):
        calculated_wind_chill = 35.74 + 0.6215 * temp - 35.75 * (velocity**0.16) + 0.4275 * temp * (velocity**0.16)
        return calculated_wind_chill

#collecting information from user
    input_degrees = float(input('What is the temperature? '))
    input_scale = input('Fahrenheit or Celsius (F/C)? ')

#getting the temperature into the right scale.
    if input_scale.lower() == 'c':
        t = convert_to_f(input_degrees)
        

    elif input_scale.lower() == 'f':
        t = input_degrees

#provision to restart program if user puts in anything other than f or c
    else: 
        restart = input('Invalid entry. Would you like to try again (y/n)? ')
        if restart.lower() == 'y':
            script()
        elif restart.lower() == 'n':
            sys.exit()     

#put the user information into the wind speed equation
    for x in range (5, 61, 5):
        wind_chill = find_wind_chill(temp = t, velocity = x)
        print(f'At temperature {t:.1f}F, and wind speed {x} mph, the windchill is: {wind_chill:.2f}F')
    
script()
import os
os.system('cls')

percentage = float(input('What is your grade percentage? '))
if percentage >= 90:
    letter = 'A' 
elif percentage >= 80:
    letter = 'B'
elif percentage >= 70:
    letter = 'C'
elif percentage >= 60:
    letter = 'D'
else:
    letter = 'F'

#logic to figure +/-
if percentage % 10 >= 7:
    sign = '+'
elif percentage % 10 <3:
    sign = '-'
else:
    sign = ' '

#logic to account for no A+, F+ or F-  
if percentage > 97:
    sign = ' '
if percentage < 60:
    sign = ' '

print(f'\nYour grade is: {letter} {sign}')

#to account for if they passed the class.
if percentage >= 70:
    print('You passed the class. Good job!')
else:
    print('Sorry, you did not pass. Try again!')

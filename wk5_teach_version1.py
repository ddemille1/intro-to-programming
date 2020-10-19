import os
os.system('cls')

percentage = float(input('What is your grade percentage? '))
if percentage >= 90:
    print('You have an A!')
elif percentage >= 80:
    print('You have a B')
elif percentage >= 70:
    print('You have a C')
elif percentage >= 60:
    print('You have a D')
else:
    print('You have an F :(\n')

if percentage >= 70:
    print('You passed the class. Good job!')
else:
    print('Sorry, you did not pass. Try again!')

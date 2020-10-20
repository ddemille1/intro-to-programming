#wk 6 teach activity
#roller coaster admission calculator
import os
os.system('cls')
first_age = int(input('What is the age of the first rider? '))
first_height = int(input('What is the height (in inches) of the first rider? '))
is_second = input('Is there a second rider (yes/no)? ')
if is_second.lower() == 'yes':
    second_age = int(input('What is the age of the second rider? '))
    second_height = int(input('What is the height (in inches) of the second rider? '))
    if second_height < 36:
        can_ride = False
    elif first_age >= 18 or second_age >= 18:
        can_ride = True
    else:
        can_ride = False
else:
    if first_age >= 18 and first_height >= 62:
        can_ride = True
    else:
        can_ride = False
if can_ride:
    print('Have a fun ride!')
if not can_ride:
    print('Sorry, you may not ride.')
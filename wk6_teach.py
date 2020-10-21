#wk 6 teach activity
#roller coaster admission calculator

import os
os.system('cls')
first_age = int(input('What is the age of the first rider? '))

#start applying golden passport condition
if first_age >= 12 and first_age <= 17:
    passport_first = input('Does first rider have a golden passport (yes/no)? ')
    if passport_first.lower() == 'yes':
        first_age = 18
#end applying golden passport condition
  
first_height = int(input('What is the height (in inches) of the first rider? '))
is_second = input('Is there a second rider (yes/no)? ')

#two riders
if is_second.lower() == 'yes':
    second_age = int(input('What is the age of the second rider? '))
    if second_age >= 12 and second_age <= 17:
        passport_second = input('Does second rider have a golden passport (yes/no)? ')
        if passport_second.lower() == 'yes':
            second_age = 18
    second_height = int(input('What is the height (in inches) of the second rider? '))
    if second_height < 36 or first_height < 36:
        can_ride = False
    elif first_age >= 18 or second_age >= 18:
        can_ride = True
    elif first_age < 18 and second_age < 18:
        if first_age >= 12 and second_age >= 12 and first_height >= 52 and second_height >= 52:
            can_ride = True
    elif first_age < 18 and second_age < 18 and first_age >= 16 and second_age >= 14:
        can_ride = True
    elif first_age < 18 and second_age < 18 and first_age >= 14 and second_age >= 16:
        can_ride = True
    else:
        can_ride = False

#one rider only
else:
    if first_age >= 18 and first_height >= 62:
        can_ride = True
    else:
        can_ride = False

#print results
if can_ride:
    print('Have a fun ride!')
if not can_ride:
    print('Sorry, you may not ride.')

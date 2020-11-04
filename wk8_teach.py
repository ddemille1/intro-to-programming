import random

repeat = True
while repeat: 
    magic_number = random.randint(1, 100)
    print(magic_number)
    guess = int(input('What is your guess (from 1-100)? '))
    x = 1  
    while magic_number != guess:
        x = x + 1
        if magic_number > guess:
            print('Higher')
            guess = int(input('What is your guess? '))
        elif magic_number < guess:
            print('Lower')
            guess = int(input('What is your guess? '))
    print('You guessed it!')
    print(f'It took you {x} tries')
    repeat = input('Do you want to play again(yes/no)? ')
    if repeat.lower() == 'yes':
        repeat = True
    else: 
        repeat = False
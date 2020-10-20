def script():
    #program code here..
    import os
    os.system('cls')

    print('Welcome to Alone!')
    print('     After spending a lifetime honing your survival skills you are selected to be a contestant on the next season of the TV series “Alone”. In this game you will test yourself against nature by trying to survive alone in the arctic beginning on September 8. If you can stay in the wild longer than the other contestants you will be given the grand prize of 3.141592 million dollars! You must leave the game if the judges determine that staying will be hazardous to your health.\n     Your site will be located near a lake in a forest. There are several species of large and small game animals in the area as well as various predators.  All contestants will be given some basic survival gear plus the option to bring one of two additional items. Will you bring a HATCHET or a BOW AND ARROW? ')
    first_level = input('Indicate your choice by typing in HATCHET or BOW AND ARROW: ')
    if first_level.lower() == 'hatchet':
        secont_level_1 = input('     You say goodbye to your family, take your gear, including your HATCHET, and report to studio headquarters. After orientation you are flown by bush plane to your campsite. What is the first thing you’ll do when you get there? Use your hatchet to make a FIRE or SHELTER? ')
    else:
        second_level_2 = input('     You say goodbye to your family, take your gear, including your bow and arrow, and report to studio headquarters. After orientation you are flown by bush plane to your campsite. What is the first thing you’ll do when you get there? Will you test your archery skills and go hunting or worry about that later and find a water source now? HUNT or WATER? ')
    restart = input('Would you like to play again? ')
    if restart.lower == 'yes':
        script()
    if restart.lower == 'no':
        print('Game over. Goodbye.')
script()

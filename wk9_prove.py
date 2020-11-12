import os
os.system('cls')

print('Welcome to the Shopping Cart Program!\n')
item_names = [] 
repeat = True
while repeat:
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View Cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = int(input('plese enter an action: '))
    if action == 1:
        item = input('What item would you like to add? ')
        item_names.append(item)
        print(f"'{item}' has been added to the cart.\n")
    elif action == 2:
        print('The contents of your shopping cart are: ')
        for item in item_names:
            print(item)
        print()
    elif action == 5:
        print('Thank you. Good bye.')
        repeat = False

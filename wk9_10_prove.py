import os
os.system('cls')

print('Welcome to the Shopping Cart Program!\n')
item_names = [] 
item_prices = []
item = None
price = None

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
        price = float(input(f"What is the price of the '{item}'? "))
        item_prices.append(price)
        print(f"'{item}' has been added to the cart.\n")
    
    elif action == 2:
        print('\nThe contents of your shopping cart are: ')
        for i in range(len(item_names)):
            item = item_names[i]
            price = item_prices[i]
            print(f'{i+1}. {item} - ${price:.2f}')
        print()

    elif action == 3:
        index = int(input('Which item would you like to remove? '))
        if index in range(len(item_names)+1):
            item_names.pop(index-1)
            item_prices.pop(index-1)
            print('Item removed.\n')
        else:
            print('Sorry, that is not a valid item number.')

    elif action == 4:
        sum = 0
        for i in range(len(item_prices)):
            price = item_prices[i]
            sum += price
        print(f'The total price of the items in the shopping cart is ${sum:.2f}\n')
        print()

    elif action == 5:
        print('Thank you. Good bye.')
        repeat = False
    
    else:
        print('Sorry, that is not a valid choice.\n')
    
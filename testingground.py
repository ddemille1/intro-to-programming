# import os
# os.system('cls')

# shopping_cart = []

# print('Please enter the items of the shopping list (type: quit to finish): ')

# run = True
# while run:
#     item = input('Item: ')
#     shopping_cart.append(item)
#     if item.lower() == 'quit':
#         shopping_cart.pop()
#         run = False
    
# print()

# print('The shopping list is: ')
# for i in shopping_cart:
#     print(i)
# print()

# print('The shopping list with indexes is:')
# for i in range(len(shopping_cart)):
#     item = shopping_cart[i]
#     print(f'{i}. {item}')
# print()

# i = int(input('Which item would you like to change? '))
# replacement = input('What is the new item? ')

# shopping_cart[i] = replacement

# print('\nThe shopping list with indexes is:')
# for i in range(len(shopping_cart)):
#     item = shopping_cart[i]
#     print(f'{i}. {item}')
# print()
import os
os.system('cls')

account_names = []
account_balances = []
name = None
balance = 0

print('Enter the names and balances of bank accounts (type: quit when done)')


while name != 'quit': 
    name = input('What is the name of this account? ')   
    if name.lower() != 'quit':
        account_names.append(name) 
        balance = float(input('What is the balance? '))
        account_balances.append(balance)



print('\nAccount information:')
for i in range(len(account_balances)):
    print(f'{i+1}. {account_names[i]} - ${account_balances[i]}')

total = 0
for i in range(len(account_balances)):
    balance = account_balances[i]
    total += balance

average = total/(len(account_balances))    

highest_name = None
highest_balance = -1
for i in range(len(account_names)):
    name = account_names[i]
    balance = account_balances[i]
    if balance > highest_balance
        highest_balance = balance
        highest_name = name


print(f'\nTotal: ${total:.2f}')
print(f'Average: ${average:.2f}')
print(f'Highest balance: ${biggest:.2f}')
import os
os.system('cls')

child_cost = float(input("\nWhat is the price of a child's meal? "))
#\n so the program isn't all bunched up at the top of the screen and is easier to read.
#used "" because there is a ' in the sentence.
adult_cost = float(input("What is the price of an adult's meal? "))
child_number = int(input('How many children are there? '))
adult_number = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))
#is it possible to put a % after the user's input?

subtotal = (child_cost*child_number + adult_cost*adult_number)
print(f'\nSubtotal: ${subtotal:.2f}')
sales_tax = tax_rate * subtotal / 100
print(f'Sales Tax: ${sales_tax:.2f}')
total = subtotal + sales_tax
print(f'Total: ${total:.2f}')

payment = float(input('\nWhat is the payment amount? '))
change = payment - total
print(f'Change: ${change:.2f}')
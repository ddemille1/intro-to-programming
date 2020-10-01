child_cost=float(input("\nWhat is the price of a child's meal? "))
#\n so the program isn't all bunched up at the top of the screen and is easier to read.
#used "" because there is a ' in the sentence.
adult_cost=float(input("What is the price of an adult's meal? "))
child_number=int(input('How many children are there? '))
adult_number=int(input('How many adults are there? '))
tax_rate=float(input('What is the sales tax rate? '))
subtotal=(child_cost*child_number + adult_cost*adult_number)
print(f'\nSubtotal: ${subtotal}')


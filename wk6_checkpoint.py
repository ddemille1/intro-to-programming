# loan qualification program
# to clear screen before starting program
import os
os.system('cls')

#input information into variables
print('Welcome to the loan calculator. \nPlease answer the following questions with a number from 1 to 10: ')
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

#calculations
if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        gets_loan = True
    
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            gets_loan = True
        else:
            gets_loan = False
    else:
        gets_loan = False

elif loan_size < 5:
    if credit_history < 4:
        gets_loan = False
    elif income >= 7 or down_payment >= 7: 
        gets_loan = True
    elif income >= 4 and down_payment >= 4:
        gets_loan = True
    else:
        gets_loan = False
else:
    gets_loan = False         

#display final result
if gets_loan:
    print('You are approved for the loan!')  
if not gets_loan:
    print('Sorry, you are not approved for the loan.')

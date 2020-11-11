import os
os.system('cls')

numbers = []
print('Enter a list of numbers, type 0 when finished.\n')

number = ''
count = 0
while number != 0:
    number = int(input('Enter number: '))
    numbers.append(number)
    count = count + 1

sum = 0
for number in numbers:
    sum += number

average = sum/(count - 1)

print(f'The sum is: {sum}')
print(f'The average is: {average}')
print(f'The largest nubmer is: {max(numbers)}')


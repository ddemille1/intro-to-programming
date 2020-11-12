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

numbers.remove(0)
sum = 0
for number in numbers:
    sum += number

average = sum/(count-1)

print(f'The sum is: {sum}')
print(f'The average is: {average:.3f}')
print(f'The largest number is: {max(numbers)}')
print(f'The smallest positive number is: {min([number for number in numbers if number > 0])}')
print('The sorted list is: ')
numbers.sort()
for number in numbers:
    print(number)






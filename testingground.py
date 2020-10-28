size  = int(input('How many columns and rows do you want in your multiplication table? '))
#range = range(1, size + 1)
#for x in range:
#    print (x, end=' ')
biggest_number = (size ** 2)
print(biggest_number)
import math
digit_count = int(math.log10(biggest_number)) + 1
print(digit_count)

for row in range(1, size +1):
    for column in range(1, size +1):
        number = row * column
        print(f'{number:}', end=' ')
    print()

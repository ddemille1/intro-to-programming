size  = int(input('How many columns and rows do you want in your multiplication table? '))
range = range(1, size + 1)
#for x in range:
#    print (x, end=' ')
for row in range:
    for column in range:
        number = row * column
        if size >= 10:
            print (f'{number:3}', end=' ')
        else:
            print (f'{number:2}', end=' ')
    print()

#other version
# size  = int(input('How many columns and rows do you want in your multiplication table? '))
# biggest_number = (size ** 2)
# print(biggest_number)
# import math
# digit_count = int(math.log10(biggest_number)) + 1
# print(digit_count)

# for row in range(1, size + 1):
#     for column in range(1, size + 1):
#         number = row * column
#         print(f'{number:{digit_count}}', end=' ')
#     print()
# #don't forget that you can put variables inside of variables with {} ex {number:{digit_count}}
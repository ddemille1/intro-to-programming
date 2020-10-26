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


#while x <= (size):
#    print('\n')
 #   for x in range:
  #      print (x, end='')
 #   x = x + 1

#for x in range:
#    print(x+1, end='')

#while x in range <= (size + 1):
#    print(x)
#    x = x + 1
#while x <= size:
#    print(x * (x+1))

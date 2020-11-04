fav_number = int(input('What is your favorite number? '))

x = 0
for i in range(0, fav_number + 1):
    x = x + i

print(f'The sum of the numbers from 0 to {fav_number} is: {x}')
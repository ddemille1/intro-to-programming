colors = ["red", "blue", "green", "yellow"]
for items in colors:
    print(items)

for x in range(1, 9):
    print(x)

candy = 'no'
while candy.lower() == 'no' or candy == 'no ' or candy == 'n':
    candy = input('May I have a piece of candy? ')
print('Thank you!')  
people = ["Stephanie 36", "John 29", "Emily 24", "Gretchen 54", "Noah 12", "Penelope 32", "Michael 2", "Jacob 10"]

youngest = 100
youngest_name = ""
oldest = -1
oldest_name = ""

for person in people:
    parts = person.split(" ")
    name = parts[0]
    age = int(parts[1])
    if age < youngest:
        youngest = age
        youngest_name = name
    if age > oldest:
        oldest = age
        oldest_name = name
print(f'The youngest person is {youngest} years old. Their name is: {youngest_name}.')
print(f'The oldest person is {oldest} years old. Their name is: {oldest_name}.')
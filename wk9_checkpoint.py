friends = []

friend = ""
while friend.lower() != "end":
    friend = input("Type the name of a friend or END to stop: ")
    if friend.lower() != "end":
        friends.append(friend)

print('\nYour friends are:')
for friend in friends:
    print(friend)
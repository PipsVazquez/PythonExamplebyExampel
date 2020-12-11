'''
Ask the user to enter the names of three people they want to
invite to a party and store them in a list. After they have entered
all three names, ask them if they want to add another. If they do,
allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party.
'''

guess = []
n = 0

for iterations in range(0, 3):
    name = input('Enter the name of the people: ')
    guess.append(name)

print('Do you want to add another guess, press [y]es or [n]')
option = input()
option = option.lower()

while option == 'y':
    name = input('Enter the name of the people: ')
    guess.append(name)

    option = input('Do you want to add other name: ')

    
for i in guess:
    n += 1
    print(f'Guess {n} is: {i}')

print('')
print('Program over')
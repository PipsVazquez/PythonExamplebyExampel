'''
Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again.
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
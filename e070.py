'''
Add to program 069 to ask the user to enter a number and
display the country in that position.
'''
countries = ('mexico', 'denmark', 'usa', 'poland', 'ukraine', 'brazil')
n = 0

print('''These are the countries of the program: ''')
for countrie in countries:
    print(n, countrie)
    n += 1
print('''Select one number to know which countrie is it''')


choice = int(input())

for index in range(0, 6):
    if index == choice:
        print(f'The counetrie {choice} is {countries[choice]}')
        break
'''
if choise in countries:
    index = countries.index(choise)
    print(f'The countrie {choise} is in {index}')
    '''

print(' ')
print('The program is over')
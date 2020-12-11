

countries = ('mexico', 'denmark', 'usa', 'poland', 'ukraine')
n = 0

print('''These are the countries of the program: ''')
for countrie in countries:
    print(n, countrie)
    n += 1

choise = input('Please enter one countrie to know the index of it')
choise = choise.lower()

if choise in countries:
    index = countries.index(choise)
    print(f'The countrie {choise} is in {index}')
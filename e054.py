import random

options = ['H','T']

tried_coin = random.choice(options)

print('''
    Welcome to the head or tails games.
    Please select [h] for head and [t] for tails
    If you guess ¡YOU WIN!
''')

choice = input()
choice = choice.upper()


if choice == tried_coin:
    print('You win')

else:
    print('Bad Luck')
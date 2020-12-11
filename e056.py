import random

number_random = random.randint(1,10)

print('''
    Welcome to guess the number
    Please enter a number between 1 and 5
    If you guess ¡YOU WIN!
''')

guess_number = int(input())


while guess_number != number_random:

    if guess_number == number_random:
        break
    
    print('''
    Select another number

    ''')
    guess_number = int(input())
    
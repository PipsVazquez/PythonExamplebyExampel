print('You going to have a party!')
print('Please enter a number below 10')

number_menu = int(input())

if number_menu <= 10:
    for counter in range(number_menu):
        print('Please enter the guess names')
        guess_names = input()
        print(f'{guess_names} has been invited')

else:
    print('Too many people')


print('')
print('Program Finished')
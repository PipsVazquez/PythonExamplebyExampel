

total = 0

for counter in range(5):
    print('Please enter a number')
    number = int(input())

    print('Press [Y] to add the number and press [N] to don\'t')
    menu = input()
    menu = menu.upper()

    if menu == 'Y':
        total = total + number
    else:
        total = total

print('Program finished')
print(f'The total add is {total}')
print('We going to make a down or up counter')
print('''

    Please enter one option:
    [U]P
    [D]own

''')
menu = input()
menu = menu.upper()

if menu == 'U':
    print('Plase enter the top number of the counter')
    number = int(input())
    for counter in range(number):
        print(counter+1)

elif menu == 'D':
    print('Plase enter a number bigger than 20')
    number = int(input())
    for counter in range(number,0,-1):
        print(counter)

else:
    print('I don\'nt understand')

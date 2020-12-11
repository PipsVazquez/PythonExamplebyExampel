import math


print( '''
    Hello, we can calculate the area of some shapes. Please selecet which area do you want to have:

    [1] Square
    [2] Triangle
    
''')

option_menu = input()

if option_menu == '1':
    shape = 'Square'
    print('You select Square, please enter the next values to have the area')
    print('Enter the length of the side')
    side_square = int(input())
    area = side_square ** 2 

elif option_menu == '2':
    shape = 'Triangle'
    print('You select Triangle, please enter the next values to have the area')
    print('Enter the length of the base')
    base_triangle = int(input())
    print('Enter the length of the base')
    height_triangle = int(input()) 

    area = (base_triangle * height_triangle) / 2

else:
    print('This option is not avaible')

print(f'The area of {shape} is {area}')
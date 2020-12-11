
option = 'y'
print('Please enter a number')
number_one = int(input())
print('')

total = number_one 

while option == 'y':
    print('Please enter another number')
    number_insert = int(input())

    #total = number_one + number_insert
    
    total = total + number_insert
       
    
    print('Do you want to continue? Press [y] to continue')
    option = input()


print(f'Program finished, the total is {total}')
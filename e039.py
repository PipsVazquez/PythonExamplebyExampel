print('Please enter a number between 1 and 12 and I will show you the table of that value')

number = int(input())
print('')

for table in range(1,11):
    print(number * table)
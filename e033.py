
print('''Welcome to this exercise. Enter 2 numbers and 

    I will show you how many times the second divides the first number and which number is the remind. 
    
    Let's do this!
''')

print('Please enter de first number')
first_number = int(input())

print('Please enter the second number')
second_number = int(input())

division = first_number // second_number
reminder = first_number % second_number



print(f'The {first_number} divided by {second_number} is {division} with {reminder} remainging')
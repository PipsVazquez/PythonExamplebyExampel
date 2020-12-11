compnum = 50
counter = 0

number_input = int(input('Please enter a number: '))


while number_input != compnum :
    number_input = int(input('Please enter a number: '))

    counter += 1


print(f'Well done you took {counter} attempts')
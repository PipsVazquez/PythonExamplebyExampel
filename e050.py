
print('Enter a number: ')
number_input = int(input())


while number_input < 10 or number_input > 20:
    print('Enter a another number: ')
    number_input = int(input())

    if number_input < 10:
        print('Number too low!')

    elif number_input > 20:
        print('Number too high!')


print('Thank you!')

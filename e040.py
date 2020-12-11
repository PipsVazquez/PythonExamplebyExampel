print('Please enter a number to make a down counter')
number = int(input())

if number <= 50 :
    for count in range(number, 0, -1):
        print(count)


else:
    print('your number is too high, try again')


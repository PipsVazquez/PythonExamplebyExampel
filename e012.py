#Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show
#the first number first and then the second.

print('Please select number 1:')
number1 = int(input())

print('Please select number 2:')
number2 = int(input())

if number1 > number2:
    #expression1
    print(f'Number {number2} is greater than number {number1}')

else:
    #expression2
    print(f'Number {number1} is less than number {number2}')

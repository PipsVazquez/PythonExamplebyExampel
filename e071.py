'''
Create a list of two sports. Ask the user what their favourite sport is and
add this to the end of the list. Sort the list and display it.
'''

sports = ['tennis', 'crossfit']

print('These are the sports:')
for i in sports:
    print(i)

option = input('Enter an other sport: ')
sports.append(option)
sports.sort()

print(sports)
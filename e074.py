'''Enter a list of ten colours. Ask the user for a starting
number between 0 and 4 and an end number between 5 and 9. Display
the list for those colours between the start and end numbers the 
user input.'''

colors = ['red', 'blue', 'yellow', 'purple', 'green', 'gray', 'black', 'white', 'brown', 'orange',]

start = int(input('Select a number between 0 to 4'))

finish = int(input('Select a number between 5 to 9'))

for showcolors in range(start, finish+1):
    print(colors[showcolors])
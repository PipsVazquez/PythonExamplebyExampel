#Ask the user to enter a
#number between 10 and 20
#(inclusive). If they enter a
#number within this range,
#display the message “Thank
#you”, otherwise display the
#message “Incorrect
#answer”.

print('Enter a number between 10 and 20')
number = int(input())

if number >= 10 and number <= 20:
    print('Thank you!')

else: 
    print('Incorrect Answer')
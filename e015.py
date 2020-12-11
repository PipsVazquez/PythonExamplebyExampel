#Ask the user to enter their favourite colour. If they enter “red”, “RED” or
#“Red” display the message “I like red too”, otherwise display the message
#“I don’t like [colour], I prefer red”.

print('Please tell me, what is your favorite color:')
color = input()

if color == 'RED' or color == 'Red' or color == 'red':
    print(f'I like {color} too')
else:
    print(f'I dont like {color}, I prefered red')
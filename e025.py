# Ask the user to enter their first name. If the length
#of their first name is under five characters, ask
#them to enter their surname and join them
#together (without a space) and display the name
#in upper case. If the length of the first name is five
#or more characters, display their first name in
#lower case.

print('Enter your name:')
name = input()

lenght_name = len(name)

if lenght_name < 5:
    print('Enter your surname:')
    surname = input()
    complete_name = name + surname 
    print(complete_name.upper())

else:
    print(name.lower())
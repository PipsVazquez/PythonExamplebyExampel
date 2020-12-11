print('Please enter your name')
name = input()
print('')

print('Now enter a number to see the magic. The number needs to be lower than 10')
repeats = int(input())

if repeats <= 10:
    for counter in range(repeats):
        print(name)

else:
    print('Number too high!')
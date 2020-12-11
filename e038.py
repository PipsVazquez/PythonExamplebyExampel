print('I will show you the magic. Please enter your name!')
name = input()

print('Please enter the times you want to see repeated')
times = int(input())

for repeats in range(times):
    for letters in name:
        print(letters)
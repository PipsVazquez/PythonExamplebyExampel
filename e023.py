#Ask the user to type in the first
#line of a nursery rhyme and
#display the length of the string.
#Ask for a starting number and an
#ending number and then display
#just that section of the text
#(remember Python starts
#counting from 0 and not 1).

print('Enter a nursery rhyme:')
nursery_rhyme = input()

lenght_nursery_rhyme = len(nursery_rhyme)

print(f'The lenght of the nursery rhyme is {lenght_nursery_rhyme}')

start_number = int(input('Enter a starting number: '))

print(nursery_rhyme[start_number : lenght_nursery_rhyme])


print('Enter a word:')
word = input()
word_lenght = len(word)

if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    #espresion
    new_word = word[1:word_lenght]+word[0]+'way'
    print(new_word.lower())

else: 
    new_word = word[1:word_lenght]+word[0]+'ay'
    print(new_word.lower())
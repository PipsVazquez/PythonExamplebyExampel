import random

points = 0
questions = 0

questions = ['¿Cuánto es la suma de 2 + 7?',
            '¿Cuánto es la resta de 7 - 2?',
            '¿Cuánto es 15 dividido entre 3?',
            '¿Cuál es la raíz cúbica de 8?',
            '¿Cuánto es 8 x 9?']



answer = ['9', '5', '5', '2', '72']


random_question = random.choice(questions)
index_question = random_question.index(str(questions))
print(index_question)

print(random_question)

answer_guess = str(input())


while questions < 5:
    if answer_guess == answer[index_question]:
        print('Correct Answer')
        points += 1
    else: 
        print('Incorrect Answer')

    questions += 1

print(f'Your points are: {points}')
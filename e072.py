'''Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again. '''

subjects = ['spanish', 'math', 'english', 'biology', 'tech', 'sports']

for subject in subjects:
    print(f'The subject is {subject}')

delete = input('Which doesnt like you')
delete = delete.lower()


position = subjects.index(delete)

del subjects[position]

print(subjects)
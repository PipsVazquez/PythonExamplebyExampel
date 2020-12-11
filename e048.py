
invitation_question ='y'
invite_counter = 0


while invitation_question == 'y':
    print('Please enter your name who want to invite to a party:')

    invite = input()

    print(f'{invite} has now been invited')

    invite_counter += 1

    invitation_question = input('Do you want to continue? Enter [y] to continue or other letter to finish: ')

print(f'{invite_counter} are going to come!')
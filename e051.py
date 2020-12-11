
green_bottles = 10 




while green_bottles > 0 :
    
    print(f'There are {green_bottles} green bottles hanging on the wall and if 1 green bottle should accidentally fall')
    green_bottles -= 1
    
    print('How many green bottles will be hanging on the wall?')
    answer = int(input())

    if answer == green_bottles:
        print(f'There will be {green_bottles} green bottles hanging on the wall')
    
    else:
        while answer != green_bottles:
            print('No try_again')
            print('How many green bottles will be hanging on the wall?')
            answer = int(input())

print(f'{green_bottles}')
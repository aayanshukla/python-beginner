print('Hello user')
name=input('Enter your name--> ')
print(f"Hello {name}")

# ask for guess game and execute the game

game=input('Would you like to play game? [y/n] -->')
secret_number = 7
if game.upper() == "Y" :
    print('Guess the secret number!!')
    guess_count=0
    guess_limit=3
    while guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count += 1
        if guess == secret_number:
            print('You won!!')
            break
    else:
        print('You lost!!')
else:
    print('NO GAME NO PROBLEM!!')

print('Hello user')
name=input('Enter your name--> ')
print(f"Hello {name}")
print('"In [y/n] dialogue boxes press y if yes or n for no!!"')

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

# making weight coverter

wtcvt=input('Would you like to covert your weight? [y/n]')
if wtcvt.upper()=="Y":
    weight=int(input('Enter your weight--> '))
    print('Press [k] to covert in kg or Press [l] to convert in lbs')
    cvt_factor=input('Do you want convert the weight entered in [k]g or [l]bs? ')
    if cvt_factor.upper()== "L":
        converter= weight/0.45
        print('Your wieght in lbs is -->',converter)
    else:
        converter=weight*0.45
        print('Your weight in kg is -->',converter)
else:
    print('Okay no weight conversion')

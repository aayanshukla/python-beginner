print('Hello user')
name=input('Enter your name--> ')
print(f"Hello {name}")

#adding while loop for all commands

quit_cmd=True

while quit_cmd:
    print("""

In [y/n] dialogue boxes press y if yes or n for no!!

    """)
    print('What would you like to do? ')
    print("""
    1. Guess game!
    2. Weight convertor
    3. Car game
    4. Quit
    """)
    select=(input('Enter command number--> '))

    # ask for guess game and execute the game

    try:
        cmd_no=int(select)
    except:
        print('Enter command *number* ')
        quit()
    if cmd_no == 1:
        print('Guess game!')
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

    elif cmd_no==2:
        print('Weight convertor!')
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

    #adding car game!!!

    elif cmd_no==3:
        car_game=input('Would you like to play the "Car game!!"? --> ').lower()
        if car_game=="y":
                    print('Car game!!!')
                    command=""
                    start=False
                    while True:
                        command=input('> ').lower()
                        if command=="start":
                            if start:
                                print('Car already started!')
                            else:
                                start=True
                                print('Car started ... Ready to go!!')
                        elif command=="stop":
                                if not start:
                                    print('Car already stopped!')
                                else:
                                    start=False
                                    print('Car stopped!')
                        elif command=="help":
                                    print("""
start- To start the car!
stop- To stop the car!
quit- To quit the game
                        """)
                        elif command == "quit":
                            break
                        elif cmd_no==4:
                            print('Quit')
                        else:
                            print('Sorry I didnt understand that :(')
        else:
            print('No game No life!!')


    exit_app=input('Would you like to exit the app? [y/n] -->')
    if exit_app.lower()=="y":
        print("""
SAYONARA!!!
""")
        quit_cmd=False
    else:
        quit_cmd=True

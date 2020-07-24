cel=int(input('Enter tempreture--> '))
print('Press [C] for Celsuis or [F]arhenheit')
convt_fact=input('Would you like to convert the following tempreture in [C]elsuis or [F]arhenheit? ')
if convt_fact=="f".lower():
    tempreture=(9/5)*cel+32
    print(f'Tempreture in Farhenheit is {tempreture} Farhenheit')
else:
    tempreture=(5/9)*cel-32
    print(f'Tempreture in Celsuis is {tempreture} Celsuis')

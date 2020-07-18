print('Hello Aayan')
hour=input('Enter hour: ')
rate=input('Enter rate: ')
try:
    fh=float(hour)
    fr=float(rate)
except:
    print('Enter a numeric value')
reg= fh*fr
if fh > 40:
    ovtp = (fh-40)*(fr*0.5)
    pay = reg+ovtp
    print('Pay:',pay)
else:
    print('Pay:',reg)

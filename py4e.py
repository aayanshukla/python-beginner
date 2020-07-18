print('Hello Aayan')
hour=input('Enter hour: ')
rate=input('Enter rate: ')
fh=float(hour)
fr=float(rate)
reg= fh*fr
if fh > 40:
    ovtp = (fh-40)*(fr*0.5)
    pay = reg+ovtp
    print('Pay:',pay)
else:
    print('Pay:',pay)

nt1 = float(input('\nDigite a primeira nota => '))
nt2 = float(input('\nDigite a segunda nota => '))

m = (nt1+nt2)/2
print('\nA sua média é {:.1f}'.format(m))

if(m>6):
    print('\nA sua média é boa, parabéns!')
else:
    print('\nMelhore!')
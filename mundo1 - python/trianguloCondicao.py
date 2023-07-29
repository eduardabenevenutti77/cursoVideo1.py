#peça o valor de 3 retas ao usuário e informe se elas podem ser um triangulo
base = int(input('\nInforme o tamanho da base => '))
reta2 = int(input('\nInforme o tamanho da reta 2 => '))
reta3 = int(input('\nInforme o tamanho da reta 3 => '))

if((base>reta3)&(reta2<reta3)):
    print('\nÉ triangulo')
else:
    print('\nNão é um triangulo')
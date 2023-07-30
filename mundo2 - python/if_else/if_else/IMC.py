#leia o peso e altura da pessoa, calcule o seu IMC e mostre seu status
#-18.5 -> baixo peso; 18.5 a 25: peso ideal; 25 até 30: sobrepeso; 30 até 40: obesidade & +40: obesidade mórbida

print('\n\t Calcule o seu IMC!')

peso = float(input('\n Informe o seu peso => '))
altura = float(input('\n Informe a sua altura => '))

IMC = (peso/altura)

if IMC<18.5:
    print('\n Você está abaixo do peso..')
elif 18.8<IMC<24:
    print('\n Você está no peso ideal..')
elif 25<IMC<30:
    print('\n Você está em sobrepesso..')
elif 30<IMC<40:
    print('\n Você está com obesidade..')
elif IMC>40:
    print('\n Você está com obesidade mórbida..')
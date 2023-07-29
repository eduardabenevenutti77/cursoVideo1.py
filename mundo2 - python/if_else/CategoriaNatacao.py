#peça o ano de nascimento e mostre a sua categoria, de acordo com a sua idade:
# até 9 anos: mirim; até 14: infantil; até 19: junior; até 20: senior & acima: master

print('\n\t \033[1;33mDescubra a sua categoria na natação!\033[m')

AnoNasc = int(input('\n Informe o ano do seu nascimento => '))
Idade = (2023 - AnoNasc)

if Idade<=9:
    print('\n A sua categoria é mirim..')
elif 9<Idade<=14:
    print('\n A sua categoria é infantil..')
elif 14<Idade<=19:
    print('\n A sua categoria é junior..')
elif 19<Idade<=20:
    print('\n A sua categoria é senior..')
else:
    print('\n A sua categoria é master..')
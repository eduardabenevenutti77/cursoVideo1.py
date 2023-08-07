#leia o ano de aniversário de 7 pessoas, e mostre quantas pessoas ainda não atigiram a maioridade e quantas já são adultas - 21 anos
from datetime import date
print('\n\t \033[1;33mVerifique quem atingiu a maioridade \033[m\n')
anoATUAL = date.today().year
for c in range(0,7):
    anoNasc = int(input("\n Informe o ano do seu nascimento: "))
    verifica = (anoATUAL - anoNasc)
    if(verifica>=21):
        print("\n Parabénsss, você é maior de idade!!!")
    else:
        print("\n Pela lei, você é considerado menor de idade :3")

#faça um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade:
# - se ele AINDA VAI SE ALISTAR ao serviço militar;
# - se é a HORA DE SE ALISTAR;
# - se já PASSOU DO TEMPO do alistamento;
#seu programa também deverá mostrar o tempo que falta ou que passou do prazo

print('\n\t \033[1;33mAlistamento Militar!\033[m')

AnoNasc = int(input('\n Informe ao sistema o ano do seu nascimento => '))
Idade = (2023-AnoNasc)

if Idade<18:
    TempoRestante = (18-Idade)
    print('Falta {} ano/s para você se alistar!'.format(TempoRestante))
elif Idade==18:
    print(' Já está na hora de se alistar!')
else:
    Tempo = (Idade-18)
    print(' Já faz {} ano/s do seu alistamento.'.format(Tempo))

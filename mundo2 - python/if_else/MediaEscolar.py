#peça duas notas e calcule a média
#- média abaixo de 5.0: REPROVADO
#- média entre 5.0 e 6.9: RECUPERAÇÃO
#- média 7.0 ou superior: APROVADO

print("\n\t \033[1;33mCalcule a média escolar de um aluno!\033[m")

n1 = float(input('\n Informe o resultado da 1ª nota => '))
n2 = float(input(' Informe o resultado da 2ª nota => '))

media = (n1+n2)/2

if media<5:
    print('\n Estude mais no próximo ano, está reprovado!')
elif 5<media<6.9:
    print('\n Quaseee, estude para a recuperação!')
else:
    print('\n Parabéns! Você foi aprovado ;)')
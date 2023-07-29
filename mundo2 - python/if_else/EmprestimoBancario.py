#escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print("\n\t \033[1;33mVerifique se seu empréstimo será aprovado!\033[m")

valorCasa = float(input('\n Informe ao sistema o valor da casa que será comprada => '))
salarioUsu = float(input(' Informe o seu salário => '))
anoPagamento = int(input(' Informe a quantidade de tempo(anos) que será necessário para pagar pela casa => '))

meses = (anoPagamento*12)
CasaMenosTempo = (valorCasa/meses)

if CasaMenosTempo>(salarioUsu*0.3):
    print(' \033[1;31mO empréstimo será negado!\033[m')
else:
    print(' \033[1;32mParabéns, o seu empréstimo foi aprovado!! O valor da prestação será de R$ {:.3f}\033[m'.format(CasaMenosTempo))
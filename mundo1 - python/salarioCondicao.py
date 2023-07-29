#pergunta o salário de um funcionário e calcule o valor do aumento
#para salários superiores a 1.250,00 calcule o aumento de 10%
#para salários menores ou iguais o aumento é de 15$

salario = float(input('\nDigite o valor do salário => '))
if(salario>1250):
    cal = (salario*0.1)
    cal1 = (salario+cal)
    print('\nO salário anterior era de R$ {:.2f}, e após um aumento de 10% passou a ser de R$ {:.2f}'.format(salario,cal1))
if((salario<1250)|(salario==1250)):
    cal2 = (salario*0.15)
    cal3 = (salario+cal2)
    print('\nO salário anterior era de R$ {:.2f}, e após um aumento de 15% passou a ser de R$ {:.2f}'.format(salario,cal3))
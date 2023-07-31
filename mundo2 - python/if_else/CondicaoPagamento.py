#calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
#à vista dinheiro: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('\n\t \033[1;33mCondições de pagamento!\033[m')

ValorProduto = float(input('\n Informe o valor do produto => '))
print('''\n Selecione a forma de pagamento:
\n[1] à vista em  dinheiro
[2] à vista no cartão 
[3] em 2x no cartão
[4] 3x ou mais no cartão''')
OpcaoPagamento = str(input('\n Informe a opcão selecionada para o pagamento => '))

if OpcaoPagamento=='1':
    CalculoDesconto = (ValorProduto*0.1)
    DescontoAplicado = (ValorProduto-CalculoDesconto)
    print('\n Querido(a) cliente, como o seu pagamento foi realizado à vista por dinheiro. Será descontado 10% do valor da peça comprada, saindo por somente R$ {:.2f}!'.format(DescontoAplicado))
elif OpcaoPagamento=='2':
    CalculoDesconto = (ValorProduto * 0.05)
    DescontoAplicado = (ValorProduto - CalculoDesconto)
    print('\n Querido(a) cliente, como o seu pagamento foi realizado à vista por cartão. Será descontado 5% do valor da peça comprada, saindo por somente R$ {:.2f}!'.format(DescontoAplicado))
elif OpcaoPagamento=='3':
    print('\n Querido(a) cliente, como o seu pagamento foi realizado em 2x no cartão, não ocorrerá desconto no valor da peça. Sendo assim, saindo por R$ {:.2f}!'.format(ValorProduto))
elif OpcaoPagamento=='4':
    CalculoJuros = (ValorProduto * 0.2)
    JurosAplicado = (ValorProduto + CalculoJuros)
    print('\n Querido(a) cliente, como o seu pagamento foi realizado em 3x no cartão. Será cobrado um juros de 10% do valor da peça comprada, saindo por R$ {:.2f}!'.format(JurosAplicado))

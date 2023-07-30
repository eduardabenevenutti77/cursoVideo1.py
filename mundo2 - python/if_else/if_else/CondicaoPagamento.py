#calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
#à vista dinheiro: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('\n\t \033[1;33mCondições de pagamento!\033[m')

ValorProduto = float(input('\n Informe o valor do produto => '))
MetodoPagamento = str(input('\n Informe o método de pagamento - cartão ou dinheiro => '))
Parcelas = int(input('\n Informe a quantidade de parcelas => '))

if MetodoPagamento=='dinheiro':
    CalculoDesconto = (ValorProduto*0.1)
    DescontoAplicado = (ValorProduto-CalculoDesconto)
    print('\n Querido(a) cliente, como o seu pagamento foi realizado à vista por {}. Será descontado 10% do valor da peça comprada, saindo por somente R$ {}!'.format(MetodoPagamento,DescontoAplicado))
elif MetodoPagamento=='cartão':
    CalculoDesconto = (ValorProduto * 0.05)
    DescontoAplicado = (ValorProduto - CalculoDesconto)
    print('\n Querido(a) cliente, como o seu pagamento foi realizado à vista por {}. Será descontado 5% do valor da peça comprada, saindo por somente R$ {}!'.format(MetodoPagamento, DescontoAplicado))
elif Parcelas<=2:
    print('\n Querido(a) cliente, como o seu pagamento foi realizado em 2x no {}, não ocorrerá desconto no valor da peça. Sendo assim, saindo por R$ {}!'.format(MetodoPagamento,ValorProduto))
elif Parcelas>=3:
    CalculoJuros = (ValorProduto * 0.2)
    JurosAplicado = (ValorProduto + CalculoJuros)
    print('\n Querido(a) cliente, como o seu pagamento foi realizado em {}x no {}. Será cobrado um juros de 10% do valor da peça comprada, saindo por R$ {}!'.format(Parcelas, MetodoPagamento, JurosAplicado))
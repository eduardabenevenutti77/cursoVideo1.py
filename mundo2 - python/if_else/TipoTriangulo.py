#peça os valores laterais e mostre o tipo do triangulo
#equilatero: todos os lados igauis;
#isosceles: dois lados iguais
#escaleno: todos os lados diferentes

print("\n\t \033[1;33mDescubra o tipo do triângulo!\033[m")

lado1 = int(input('\n Informe o valor do lado 1 => '))
lado2 = int(input('\n Informe o valor do lado 2 => '))
lado3 = int(input('\n Informe o valor do lado 3 => '))

if lado1==lado2 and lado3==lado2 and lado3==lado1:
    print('\n O triângulo é equilatero..')
elif (lado1==lado2 and lado3!=lado2 and lado3!=lado1) or (lado1!=lado2 and lado3==lado2 and lado3!=lado1) or (lado1!=lado2 and lado3!=lado2 and lado3 ==lado1):
    print('\n O triângulo é isoceles..')
else:
    print('\n O triângulo é escaleno..')

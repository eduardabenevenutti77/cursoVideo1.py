#crie um progama que peça dois valores e em seguida mostre na tela o seguinte menu [1]SOMA [2]MULTIPLICAR [3]MAIOR [4]NEWNUMEROS [5]SAIRPROGRAMA
#o programa deverá realizar a operação solicitada em cada casa selecionada
maior = 0
op = 0
while op != 5:
    print("""
    [1] Adição
    [2] Multiplicação
    [3] Verifique o maior número
    [4] Novo número
    [5] Sair do programa
    """)
    op = int(input("Informe uma opção: "))

    if (op == '2'):
        n1 = float(input("\nInforme 1º valor: "))
        n2 = float(input("Informe o 2º valor: "))
        mult = (n1 * n2)
        print("\n{} X {} = {}".format(n1,n2,mult))
    elif (op == '1'):
        n1 = float(input("\nInforme 1º valor: "))
        n2 = float(input("Informe o 2º valor: "))
        adi = (n1 + n2)
        print("\n {} + {} = {}".format(n1,n2,adi))
    elif (op =='3'):
        n1 = float(input("\nInforme 1º valor: "))
        n2 = float(input("Informe o 2º valor: "))
        v1 = n1 >= n2
        v2 = n2 >= n1
        #v3 = maior >= n1
        if (v1>v2):
            print("N1 é o número maior")
        elif (v2>maior):
            print("N2 é o maior número")
    elif (op == '4'):
        print("\n Informe os valores novamente")
        v1 = int(input("Valor 01: "))
        v2 = int(input("Valor 02: "))
    elif (op == '5'):
        print("O programa será encerado..")
        exit(0)

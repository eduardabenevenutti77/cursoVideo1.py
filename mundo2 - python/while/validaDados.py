#faça um programa que leia o sexo de uma pessoa. mas que só aceita os seguintes valores: 'M' ou 'F'.
#caso esteja errado, peça a digitação novamente até receber o valor correto


c = str(input("Informe ao sistema a sua sexualidade [M|F] => ")).strip().upper()[0]
while c not in 'MF':
    c = str(input("Informe ao sistema a sua sexualidade novamente => ")).strip().upper()[0]
print("Olá, você é do gênero {}!".format(c))

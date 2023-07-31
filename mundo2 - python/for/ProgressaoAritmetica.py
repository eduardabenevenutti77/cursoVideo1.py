#leia o 1º termo e a razão de uma PA, no final mostre os 10 primeiros termos dessa progressão

print('\n\t \033[1;33mCalcelue uma progressão aritmética\033[m\n')

Termos = int(input(' Informe o valor do 1º termo => '))
Razao = int(input(' Informe a razão da P.A. =>'))
t = Termos
print(t)
for c in range(0, 9):
    t = t + Razao
    print(t)


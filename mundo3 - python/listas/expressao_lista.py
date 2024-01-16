# o usuário deve digitar uma expressão matemática que use parênteses, e o sistema deverá analisar se a expressão passada está correta ou não
# no caso, se os parênteses estão abertos e fechados na ordem certa

def verifica_parenteses(expressao):
    pilha = []
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                return False 
            pilha.pop()
    return not pilha  

expressao = input('Digite uma expressão matemática: ')
if verifica_parenteses(expressao):
    print('Os parênteses estão corretos.')
else:
    print('Os parênteses não estão corretos.')
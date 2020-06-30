n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO número é maior.')
elif n1 < n2:
    print('O SEGUNDO número é maior.')
# Como não existe uma quarta opção, a próxima linha poderia ser 'else'
elif n1 == n2:
    print('Não existe maior, os números são IGUAIS.')


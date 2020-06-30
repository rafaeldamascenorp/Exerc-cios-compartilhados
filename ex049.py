# Retomando o exercício 009 sobre a tabuada
n = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 11)
for c in range(1, 11):
    print('{} x {} = {:2}'.format(n, c, n * c))
print('-=' * 11)
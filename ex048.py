soma = 0 # acumulador (não acumulei nada até agora)
cont = 0 # contador (até agora não contei número nenhum
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c # ou soma += c
        cont = cont + 1 # ou cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
valor = float(input('Qual é o valor do imóvel? R$'))
salário = float(input('Qual é o salário do possível comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor // (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(valor, anos, prestação))
if prestação > salário * 0.30:
    print('Infelizmente seu pedido de empréstimo foi NEGADO.')
else:
    print('Empréstimo CONCEDIDO!!')
preço = float(input('Digite o preço do produto: R$'))
desc = preço * 0.90
parcelado = preço * 1.08
print('-' * 12)
print('Um produto que normalmente custa R${:.2f}, se pago à vista terá 10% de desconto. \nO preço com desconto é de R${:.2f}.'.format(preço, desc))
print('-' * 12)
print('Caso o pagamento seja parcelado, será acrescentado juros de 8%. \nO preço total do parcelamento é de R${:.2f}'.format(parcelado))
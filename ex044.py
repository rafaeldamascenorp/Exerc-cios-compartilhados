print('=' * 11, 'LOJAS GUANABARA', '=' * 11)
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pgto = int(input('Qual é a opção de pagamento: '))
if pgto == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço * 0.90))
elif pgto == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço * 0.95))
elif pgto == 3:
    print('Sua compra de R${:.2f} vai ser paga em 2x de R${:.2f} sem juros.'.format(preço, preço / 2))
elif pgto == 4:
    parcelas = int(input('Em quantas parcelas? '))
    novo = preço * 1.20
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, novo / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, novo))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')


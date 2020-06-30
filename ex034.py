salário = float(input('Qual o salário do funcionário? R$'))
if salário > 1250:
    novo = salário * 1.1
else:
    novo = salário * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}.'.format(salário, novo))

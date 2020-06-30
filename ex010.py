r = float(input('Quantos reais você tem na carteira? R$'))
d = r / 3.27
eur = r / 4.32
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(r, d))
print('Com R${:.2f} você pode comprar EUR{:.2f}.'.format(r, eur))

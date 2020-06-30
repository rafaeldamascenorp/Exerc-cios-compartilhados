larg = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de{}m²'.format(larg, alt, área))
tinta = área / 2
print('Para pintá-la, você precisará de {} litros de tinta.'.format(tinta))

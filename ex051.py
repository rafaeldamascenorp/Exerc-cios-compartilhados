print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
# Recorrendo à matemática para achar o enésimo termo de uma PA
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU')
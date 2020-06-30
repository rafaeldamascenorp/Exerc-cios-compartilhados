peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está na faixa de PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')
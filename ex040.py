n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, média))
if média < 5.0:
    print('O aluno está REPROVADO.')
elif 5.0 <= média < 7.0:
    print('O aluno está em RECUPERAÇÃO.')
elif média >= 7.0:
    print('O aluno está APROVADO.')
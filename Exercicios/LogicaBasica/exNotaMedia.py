m1 = float(input('Digite a nota1 '))
m2 = float(input('Digite a nota2 '))
m3 = float(input('Digite a nota3 '))

media = (m1+m2+m3)/3
notaArredondada = round(media, 1)

if media >= 0 and media <= 4:
    print(f'o aluno esta com a media {notaArredondada}, por isso ele esta reprovado')
elif media >= 4.1 and media <= 6:
    print(f'o aluno esta com a media {notaArredondada}, por isso ele esta de exame(???)')
    exame = float(input('Digite a nota do exame '))
    if exame >= 6:
        print('ele esta de APROVADO')
    else:
        print('ele esta reprovado')
elif media >= 6.1 and media >= 10:
    print(f'o aluno esta com a media {notaArredondada}, por isso ele esta de APROVADO')
else:
    print('Insira uma nota valida')
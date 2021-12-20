idade = int(input('Digite a idade'))

if idade <= 12 and idade >= 1:
    print('Criaça') 
elif idade > 12 and idade <= 18:
    print('Mongo')
elif idade > 18:
    print('Adulto')
else:
    print('Coloca um número certo!')

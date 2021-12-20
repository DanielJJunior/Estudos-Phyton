notas = 0
for i in range(1, 6):
    nota = float(input(f'Digite sua {i} nota '))
    notas = notas + nota
media = notas/5
print(f'a media é de {media}')


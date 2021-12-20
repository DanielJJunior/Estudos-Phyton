import os
while True:
    print('=============================================================================')
    print(' ')
    inputUsuario = int(input('Qual ação é desejada? \n1 - Git Status \n2 - Git add/commit/push \n3 - Visualizar arquivos no repositorio \n4 - Git rm \n5 - Git init \n6 - Git remote add \n7 - Verificar o repositório atual\n'))
    if inputUsuario == 1:
      print(os.system("git status"))
    elif inputUsuario == 2:  
          nomeArquivo = str(input('Insira o nome do arquivo/pasta desejado: '))
          commit = str(input('Insira o comentario do commit: '))

          os.system('git add '+ nomeArquivo)
          os.system('git commit -m '+'"'+ commit +'"' )
          os.system('git push')
    elif inputUsuario == 3:
          os.system('dir')
    elif inputUsuario == 4:
          nomeArquivoRemov = str(input('Insira o nome do arquivo/pasta desejado para remoção: '))
          commit = str(input('Insira o comentario do commit: '))
          
          os.system('git rm -r ' + nomeArquivoRemov)
          os.system('git commit -m '+'"'+ commit +'"' )
          os.system('git push')
    elif inputUsuario == 5:
          os.system('git init')
    elif inputUsuario == 6:
          nomeOrigem = str(input('Insira a origem do repositório: '))
          os.system('git remote add origin '+nomeOrigem)
    elif inputUsuario == 7:
          os.system('git remote -v')
    else:
        print('Ação inválida!')
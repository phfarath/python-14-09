#Pedro Henrique Pontes Farath - RM98608
try:
    f= open('d:/ditados.txt', 'a')
    print('Digite um ditado popular: ')
    ditado2=input()
    f.write(f'\n{ditado2}')
    f.close()
    f=open('d:/ditados.txt', 'r')
    print('-'*30)
    print(f'seu novo ditado diz: {f.read()}')
    print('-'*30)
    f.close()
except FileNotFoundError:
    print('arquivo nao encontrado')
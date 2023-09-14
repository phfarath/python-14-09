#Pedro Henrique Pontes Farath - RM98608
try:
    f=open("d:/ditados.txt", 'w')
    print('Digite um ditado popular: ')
    ditado= input()
    f.write(ditado)
    f.close()
    f=open("d:/ditados.txt", 'r')
    print('-'*30)
    print(f'seu arquivo diz: {f.read()}')
    print('-'*30)
    f.close()
except FileNotFoundError:
    print("File not found")
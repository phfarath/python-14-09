try:
    print('Digite seu login: ')
    login= input()
    f=open(f'd:/{login}.txt', 'r')
    print('Login aceito!')
    print('Digite sua senha: ')
    senha= input()
    for i in range(0,4,1):
        f.readline(5)
        if i == senha:
            print('Acesso concedido')
            print('-'*30)
            print(f'suas informacoes: {f.read()}')
            print('-'*30)
        
    f.close()
except FileNotFoundError:
    print('arquivo nao encontrado')
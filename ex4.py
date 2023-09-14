try:
    print('Faça seu cadastro: (y/n)')
    resp=(input()).lower()
    while resp!='n' :
        print('Digite o seu nome: ')
        nome=input()
        print('Digite seu login: ')
        login= input()
        print('Digite sua senha: ')
        senha=input()
        f=open(f'd:/{login}.txt', 'a')
        f.write(f'\n{nome}')
        f.write(f'\n{login}')
        f.write(f'\n{senha}')
        f.close()
        print('Deseja continuar? (y/n)')
        resp=input().lower()
except FileNotFoundError:
    print('arquivo nao encontrado')
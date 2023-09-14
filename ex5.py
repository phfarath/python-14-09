print ('ENTRAR')

login = input('login: ')
senha = input('senha: ')

try:
    f = open(f'd:/{login}.txt', 'r')
    f.close()
except OSError:
    print('login inválido ')
    login = input('login: ')
    senha = input('senha: ')
f = open(f'd:/{login}.txt', 'r')
validar = f.readline()
usuario1 = f.readline()
senha1 = f.readline(10)
f.close
while (senha1 != senha):
    print('Senha invalida')
    senha = input('senha: ')

print('Acesso concedido')
print('-'*30)
print(f'usuario: {usuario1} \nlogin: {validar}')
print('-'*30)

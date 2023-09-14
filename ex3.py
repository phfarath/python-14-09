#Pedro Henrique Pontes Farath - RM98608
f=open('d:/digitos.txt', 'w')
dict= {0}
digito=1
while digito!=0:
    print('Digite numeros inteiros (digite 0 para parar): ')
    digito=int(input())
    if digito!=0:
        dict.add(digito)
    else:
        continue
dict.remove(0)
f.write(str(dict))
f.close()
f=open('d:/digitos.txt', 'r')
print('-'*30)
print(f'sua lista: {f.read()}')
print('-'*30)
f.close()
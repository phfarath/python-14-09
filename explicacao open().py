#criar arquivo pela pasta de arquivos 
import os #funcao que apaga os arquivos 
try: 
    if os.path.exists("d:/alo.txt"):
        os.remove('d:/alo.txt')
    else:
        print('arquivo nao encontrado!')

    f=open("d:/alo.txt", "w") #colocar um arquivo inexistente vai criar um arquivo e adicionar o pedido
    f.write("\noi tubo bem?")
    f.write("\nsou pequenininha")
    f.write('\ndo tamanho de um botao')
    f.write('\no bolso furou e papai caiu no chao')
    f.write('\nMamãe que é mais querida, ficou no coração')
    
    
    f.close()
    f = open("d:/alo.txt", "r") #para leitura de arquivo com o portugues desfigurado (use enconding='utf-8')
    print(f.read())#passar a quant de carcteres lidos 
    #print(f.readline()) le linhas do arquivo 
    #for x in range(0,4,1):
        #print(f.readline())
    f.close()
except FileNotFoundError:
    print('Arquivo não encontrado!')
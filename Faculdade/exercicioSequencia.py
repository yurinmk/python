def sequecia(inicio, fim):
    #Cria uma lista vazia
    lista = []
    #lista.append incrementa o item a lista
    for i in range(inicio,fim+1):
        lista.append(i * i)
    print(lista)

def main():
    inicioDaSequencia = int(input("nº de início da sequência = "))
    fimDaSequencia = int(input("nº de fim da sequência = "))
    sequecia(inicioDaSequencia,fimDaSequencia)

main()
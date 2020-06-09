def main():
    matriz = [["","",""],["","",""],["","",""]]

    for i in range(0,9):
        print("Jogo da Velha")
        print("Nº da 1 Posição (1 a 3):")
        a = int(input()) - 1
        print("Nº da 2 Posição (1 a 3):")
        b = int(input()) - 1
        print("Insira X ou O:")
        valor = input()
        matriz[a][b] = valor
        print("P  ",1," ",2," ", 3)
        for i in range(0, 3):
            print(i+1,matriz[i])
main()
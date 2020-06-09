def main():
    matriz = [[39, 14, 27], [21, 83], [31, 12, 43]]
    print("Digite qual posição deseja excluir:")
    y = int(input()) - 1
    for i in range(len(matriz)):
        matriz[i].remove(matriz[i][y])
    print(matriz)


main()
def main():
    matriz = [[1, 5],
              [7, 3],
              [8, 2]]
    matrizTransposta = []
    for i in range(len(matriz[0])):
        matrizTemp = []
        for j in range(len(matriz)):
            matrizTemp.append(matriz[j][i])
        matrizTransposta.append(matrizTemp)
    print(matrizTransposta)
main()
def main():
    matriz = [[1,5],
              [7,3],
              [8,2]]
    matriz1 = [[]]
    matriz2 = [[]]
    matrizT = []
    for i in range(len(matriz)):
        matriz1[0].append(matriz[i][0])
        matriz2[0].append(matriz[i][1])
    matrizTransposta = matriz1 + matriz2
    print("Matriz Normal")
    for i in range(len(matriz)):
        print(matriz[i])
    print("Matriz Transposta:")
    for i in range(len(matrizTransposta)):
        print(matrizTransposta[i])
main()
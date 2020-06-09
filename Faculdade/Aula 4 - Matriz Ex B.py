def main():
    matriz = [[39,14,27],[21,83,92],[31,12,43]]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],"x 7 =",(matriz[i][j] * 7))

main()
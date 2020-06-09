def main():
    matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    x = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input(f'Digite na posição [{i}][{j}]:'))
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > 10:
                x += 1
    print("Tem",x,"número(s) maior que 10")
main()
def main():
    matriz = [[1,2,3,4],[5,6,7,8]]
    x = int(input())
    for i in range(len(matriz)):
        matriz[i].append(x)
    print(matriz)
main()
def main():
    matriz = []
    x = int(input("Quantos alunos você deseja adicionar?"))
    for i in range(0,x):
        matrizT = []
        matrizT.append(input("Nome:"))
        matrizT.append(input("Matrícula:"))
        matrizT.append(input("D. Nascimento:"))
        matriz.append(matrizT)
    print(matriz)

main()
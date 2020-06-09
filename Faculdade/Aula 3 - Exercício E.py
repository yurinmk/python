def main():
    registro = []

    for i in range(0,5):
        print("#", i + 1, "Nome:")
        registro.append(input())
    print("Nomes inseridos: ", registro)
    print("Insira um nome para ultima posição: ")
    registro.append(input())
    print("Insira um nome para 2 posição: ")
    registro.insert(1, input())
    print(registro)
main()
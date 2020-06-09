def main():
    nomes = []
    for i in range (0,5):
        print("#", i + 1, "Nome:")
        nomes.append(input())
    print(nomes)
    print("Digite o seu sobrenome:")
    nomes.insert(nomes.index("Yuri"), input())
    print(nomes)
main()
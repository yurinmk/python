
def main():

    nomes = ["Yuri","Kruba","Iria","Aline","Alana"]
    dataAniversario = ["04/12/1993", "09/02/1993", "10/10/1992", "25/12/1989", "25/12/1989"]
    entrada = 10
    while entrada != 0:
        entrada = int(input("Add Pessoas (1) | Remover Pessoas (2) | Apresentar Agenda (3) | Sair (0) \n"))
        if entrada == 1:
            qnt = int(input("Quantas pessoas deseja add? \n"))
            for i in range (qnt):
                nome = input("Nome: ")
                aniversario = input("Aniversário: ")
                nomes.append(nome)
                dataAniversario.append(aniversario)
                print("Adicionado com sucesso")
        elif entrada == 2:
            qnt = int(input("Quantas pessoas deseja remover? \n"))
            for i in range(qnt):
                reNome = input("Nome que seja remover: ")
                dataAniversario.pop(nomes.index(reNome))
                nomes.remove(reNome)
                print("Revomido com sucesso")
        elif entrada == 3:
            print("Agenda:\n")
            for i in range (0,len(nomes)):
                print(" Nome: ", nomes[i], ", Aniversário: ", dataAniversario[i])
            print()
main()
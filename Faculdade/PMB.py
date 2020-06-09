def tabela():
    print("COD do grupo | Nome do grupo")
    print("1 | Passeriformes")
    print("2 | N Passeriformes")
    print("3 | Mamíferos Placentários")
    print("4 | Marsupiais e Edentatas")
    print("5 | Répteis")
def tmb(pm, gp):
    gp1 = 129
    gp2 = 78
    gp3 = 70
    gp4 = 49
    gp5 = 10
    tmp = 0
    if gp == 1:
        tmp = (pm ** 0.75) * gp1
    elif gp == 2:
        tmp = (pm ** 0.75) * gp2
    elif gp == 3:
        tmp = (pm ** 0.75) * gp3
    elif gp == 4:
        tmp = (pm ** 0.75) * gp4
    elif gp == 5:
        tmp = (pm ** 0.75) * gp5
    return tmp

def main():
    print("Insira peso metabólico: ")
    pm = float(input())
    tabela()
    print("Insira o COD do grupo pertencente: ")
    gp = int(input())
    print("Taxa Metabólica Basal: ", tmb(pm, gp))
main()
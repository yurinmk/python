def tabela():
    print("COD do grupo | Nome do grupo")
    print("1 | Passeriformes")
    print("2 | N Passeriformes")
    print("3 | Mamíferos Placentários")
    print("4 | Marsupiais e Edentatas")
    print("5 | Répteis")
def tmb(pm, gp, letra):
    gp1 = 129
    gp2 = 78
    gp3 = 70
    gp4 = 49
    gp5 = 10
    tmb = 0

    if gp == 1 and letra == 'B':
        tmb = (pm ** 0.75) * gp1
    elif gp == 2 and letra == 'B':
        tmb = (pm ** 0.75) * gp2
    elif gp == 3 and letra == 'B':
        tmb = (pm ** 0.75) * gp3
    elif gp == 4 and letra == 'B':
        tmb = (pm ** 0.75) * gp4
    elif gp == 5 and letra == 'B':
        tme = (pm ** 0.75) * gp5
    return tmb
def tme(pm, gp, letra):
    gp1 = 129
    gp2 = 78
    gp3 = 70
    gp4 = 49
    gp5 = 10
    tme = 0
    if gp == 1 and letra == 'E':
        tme = (pm ** 0.25) * gp5
    elif gp == 2 and letra == 'E':
        tme = (pm ** 0.25) * gp5
    elif gp == 3 and letra == 'E':
        tme = (pm ** 0.25) * gp5
    elif gp == 4 and letra == 'E':
        tme = (pm ** 0.25) * gp5
    elif gp == 5 and letra == 'E':
        tme = (pm ** 0.25) * gp5
    return tme
def main():
    print("Insira peso metabólico: ")
    pm = float(input())
    tabela()
    print("Insira o COD do grupo pertencente: ")
    gp = int(input())
    print("Insira (B) Para PMB - Insira (E) Para PME: ")
    letra = input()
    if letra == 'B':
        print("Taxa Metabólica Basal: ", tmb(pm, gp, letra))
    elif letra == 'E':
        print("Taxa Metabólica Específica: ", tme(pm, gp, letra))
main()
def sheldon(v, d):
    x = False
    if v == "tesoura" and d == "papel" or d == "lagarto":
        x = True
    else:
        x = False
    if v == "papel" and d == "pedra" or d == "Spock":
        x = True
    else:
        x = False
    if v == "pedra" and d == "lagarto" or d == "tesoura":
        x = True
    else:
        x = False
    if v == "lagarto" and d == "papel" or d == "Spock":
        x = True
    else:
        x = False
    if v == "Spock" and d == "tesoura" or d == "pedra":
        x = True
    else:
        x = False
    return x
def main():
    entrada = int(input())
    for i in range (0,entrada):
        teste = input().split()
        if (teste[0] == teste[1]):
            print("Caso #3: De novo!")
        elif(sheldon(teste[0],teste[1]) == True):
            print("Caso #1: Bazinga!")
        elif(sheldon(teste[0],teste[1]) == False):
            print("Caso #2: Raj trapaceou!")
main()
def main():

    n = int(input("Valor da tabuada de x: "))
    temp = 1
    for i in range(n,0,-1):
        temp *= i
        print(temp)
main()
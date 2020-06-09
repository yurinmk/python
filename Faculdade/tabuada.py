def main():

    entrada = int(input("Tabuada de: "))
    for i in range(1, 11):
        print(entrada,"x",i,"=",(i*entrada))
    temp = 1
    while temp <= 10:
        print(entrada, "x", temp, "=", (temp * entrada))
        temp += 1
main()
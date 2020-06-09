def main():
    cores = ["azul","amarelo","vermelho","laranja","verde"]
    print(cores)
    #Verificar se existe a cor vermelho no vetor
    if cores.__contains__("vermelho"):
        cores.remove("vermelho")
    else:
        print("Não existe a cor vermelha!")
    print(cores)

main()
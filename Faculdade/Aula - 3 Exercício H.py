def main():
    dataNascimento = ["1993", "1991", "1989", "1966", "1994","1990"]
    print("Crescente: ", sorted(dataNascimento, key=int))
    print("Decrescente: ",sorted(dataNascimento, key=int,reverse=True))

main()
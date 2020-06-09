def main():
    registro = []
    print("Digite sair quando quiser parar")
    while("sair" not in registro):
        registro.append(input("Digite: "))
    registro.remove("sair")
    print(registro)
main()
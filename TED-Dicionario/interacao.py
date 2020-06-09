class Interacao:
    def __init__(self):
        self.menu0 = "0 - Sair"
        self.menu1 = "1 - Cadastrar Devedor"
        self.menu2 = "2 - Pesquisar Devedor"
        self.menu3 = "3 - Atualizar Valor"
        self.menu4 = "4 - Remover devedor"
        self.menu5 = "5 - Mostrar todos os devedores"

    def menuPrincipal(self):
        temp = "\nMenu Principal\n" + self.menu0 + "\n"  + self.menu1 + "\n" + self.menu2 \
            +"\n" + self.menu3 + "\n" + self.menu4+ "\n" + self.menu5
        return temp
class Interacao:
    def __init__(self):
        self.inicio = "\nMenu Inicial" + "\n" + "O que você deseja?"
        self.menu1 = "0 - Sair"
        self.menu2 = "1 - Logar"
        self.menu3 = "1 - Cadastrar Funcionário"
        self.menu5 = "0 - Sair"
        self.menu6 = "1 - Cadastrar Veículos"
        self.menu7 = "2 - Identificar Veículos"
        self.menu8 = "3 - Remover Veículos"
        self.menu9 = "4 - Cadastrar Eventos"
        self.menu10 = "5 - Cadastrar Ocorrencias"
        self.menu11 = " - Cadastrar Áreas Especiais"
        self.menu12 = "6 - Monitorar Estacionamento"
        self.menu13 = "7 - Monitorar Eventos"
        self.menu14 = "8 - Monitorar Ocorrencias"
        self.menu111 = "\nQual área deseja monitorar?"
        self.menu15 = "0 - Todos"
        self.menu16 = "1 - Bloco A"
        self.menu17 = "2 - Bloco B"
        self.menu18 = "3 - Bloco C"
        self.menu19 = "4 - Bloco D"
        self.menu20 = "5 - Bloco E"
        self.menu21 = "6 - Bloco F"
        self.menu22 = "7 - Bloco G"
        self.menu23 = "8 - Bloco Central"
        self.menu24 = "Em qual área?"
        self.menu25 = "2 - Dar permissão em Áreas Especiais"
        self.menu26 = "100 - Deslogar"
        self.menu27 = "1 - Cadastrar Áreas Especiais"
        self.menu28 = "2 - Monitorar Estacionamento"
        self.menu29 = "3 - Monitorar Eventos"
        self.menu30 = "4 - Monitorar Ocorrencias\n5 - Monitorar Áreas Especiais\n6 - Remover Áreas Especiais\
            \n7 - Cadastrar Eventos\n8 - Dar Permissão em Áreas Especiais\n9 - Gerar Relatórios"

        self.menu31 = "1 - Batidas"
        self.menu32 = "2 - Furto ou Assalto"
        self.menu33 = "3 - Estacionamento Indevido"
        self.menu34 = "4 - Inundação"
        self.menu35 = "5 - Dano ao Veículo"
        self.menu36 = "6 - Outros"

        self.menu37 = "1 - Funcionário"
        self.menu38 = "2 - Professores"
        self.menu39 = "3 - Convidados"
        self.menu40 = "4 - Reitores"
        self.menu41 = "5 - Outros"

        self.menu42 = "1 - Estacionamento"
        self.menu43 = "2 - Eventos"
        self.menu44 = "3 - Ocorrências"
        self.menu45 = "4 - Áreas Especias"
        
        
        
        



    def getInteracao(self):
        temp = self.inicio + "\n" + self.menu1 + "\n" + self.menu2
        return temp
    def getInteracao2(self):
        temp = self.menu5 + "\n" + self.menu6 + "\n" + self.menu7 + "\n" + self.menu8 + \
               "\n" + self.menu9 + "\n" + self.menu10 +  "\n" + self.menu12+ "\n" + self.menu13\
                   + "\n" + self.menu14 + "\n" + self.menu26
        return temp
    def getInteracao3(self):
        temp = self.menu111+"\n" + self.menu15+"\n" + self.menu16+"\n" + self.menu17+"\n" + self.menu18\
            +"\n" + self.menu19+"\n" + self.menu20+"\n" + self.menu21+"\n" + self.menu22+"\n" + self.menu23
        return temp
    def getInteracao4(self):
        temp = self.menu24+"\n"  + self.menu16+"\n" + self.menu17+"\n" + self.menu18\
            +"\n" + self.menu19+"\n" + self.menu20+"\n" + self.menu21+"\n" + self.menu22+"\n" + self.menu23
        return temp
    def getInteracaoRH(self):
        return self.menu3 + "\n" + self.menu25 + "\n" + self.menu26
    def getInteracaoGestor(self):
        return self.menu27 + "\n" + self.menu28 + "\n" + self.menu29  + "\n" + self.menu30 + "\n" + self.menu26
    def getInteracaoOcorrencias(self):
        return self.menu31  + "\n" + self.menu32  + "\n" + self.menu33  + "\n" + self.menu34  + "\n" + self.menu35 \
             + "\n" + self.menu36
    def getInteracaoAcesso(self):
        return self.menu37  + "\n" + self.menu38  + "\n" + self.menu39  + "\n" + self.menu40  + "\n" + self.menu41
    def getInteracaoRelatorios(self):
        return self.menu42  + "\n" + self.menu43  + "\n" + self.menu44  + "\n" + self.menu45
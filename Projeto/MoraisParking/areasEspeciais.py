from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

class AreasEspeciais():
    def __init__(self):
        self.bloco = ''
        self.acesso = ''
        self.inicio = ''
        self.fim = ''
        self.vagas = ''
        self.status = ''
        self.areasEspeciais = [
            ['1','Bloco A','Reitoria','01/06/2020','10/06/2020','20','Ativa'],
            ['2','Bloco C','Outros','01/06/2020','05/06/2020','10','Ativa']]
    def cadastrarAreaEspecial(self,valor,valor2,inicio,fim,vagas):
        temp = []
        y = ""
        if valor == 1:
            y = "Bloco A"
        elif valor == 2:
            y = "Bloco B"
        elif valor == 3:
            y = "Bloco C"
        elif valor == 4:
            y = "Bloco D"
        elif valor == 5:
            y = "Bloco E"
        elif valor == 6:
            y = "Bloco F"
        elif valor == 7:
            y = "Bloco G"
        elif valor == 8:
            y = "Bloco Central"

        x = ""
        if valor2 == 1:
            x = "Funcionário"
        elif valor2 == 2:
            x = "Professores"
        elif valor2 == 3:
            x = "Convidados"
        elif valor2 == 4:
            x = "Reitores"
        elif valor2 == 5:
            x = "Outros"
        temp.append(len(self.areasEspeciais) + 1)
        temp.append(y)
        temp.append(x)
        temp.append(inicio)
        temp.append(fim)
        temp.append(vagas)
        temp.append("Ativa")
        self.areasEspeciais.append(temp)
    def monitoramentoAreasEspeciaisPorBloco(self,valor,status):
        temp = ""
        y = ""
        if valor == 1:
            y = "Bloco A"
        elif valor == 2:
            y = "Bloco B"
        elif valor == 3:
            y = "Bloco C"
        elif valor == 4:
            y = "Bloco D"
        elif valor == 5:
            y = "Bloco E"
        elif valor == 6:
            y = "Bloco F"
        elif valor == 7:
            y = "Bloco G"
        elif valor == 8:
            y = "Bloco Central"
        if valor == 0:
            #For que percorre as áreas especiais
            for x in range(len(self.areasEspeciais)):
                #condição para armazenar e retornar a variável temp mediante as informações escolhidas na interação
                if status == self.areasEspeciais[x][6]:
                    temp +=  "\n| ID: " + str(self.areasEspeciais[x][0]) +" | Bloco:  " + self.areasEspeciais[x][1] +\
                            " | Acesso: " + self.areasEspeciais[x][2] + " | Inicio: " + self.areasEspeciais[x][3] + \
                                " | Fim: " + self.areasEspeciais[x][4] +" | Vagas: " + self.areasEspeciais[x][5]  +\
                                     " | Status: "+ self.areasEspeciais[x][6]  + " |\n"
        else:
            #For que percorre as áreas especiais
            for x in range(len(self.areasEspeciais)):
                #condição para armazenar e retornar a variável temp mediante as informações escolhidas na interação
                if y == self.areasEspeciais[x][1] and status == self.areasEspeciais[x][6]:
                    temp += "\n| ID: " + str(self.areasEspeciais[x][0]) + " | Bloco:  " + self.areasEspeciais[x][1] +\
                        " | Acesso: " + self.areasEspeciais[x][2] + " | Inicio: " + self.areasEspeciais[x][3] + \
                            " | Fim: " + self.areasEspeciais[x][4] +" | Vagas: " + self.areasEspeciais[x][5]  + \
                                " | Status: "+ self.areasEspeciais[x][6]  + " |\n"
        return temp
    def monitoramentoAreasEspeciaisPorTempo(self,valor):
        temp = ""
        #For que percorre as áreas especiais
        for x in range(len(self.areasEspeciais)):
            #condição para armazenar e retornar a variável temp mediante as informações escolhidas na interação
            if valor ==  self.areasEspeciais[x][5]:
                temp += "\n| ID: " + self.areasEspeciais[x][0] + " | Bloco:  " + self.areasEspeciais[x][1] +\
                        " | Acesso: " + self.areasEspeciais[x][2] + " | Inicio: " + self.areasEspeciais[x][3] + \
                            " | Fim: " + self.areasEspeciais[x][4] + " | Vagas: " + self.areasEspeciais[x][5]  +\
                                 " | Status: "+ self.areasEspeciais[x][6]  + " |\n"
            return temp
    def removerAreaEspecial(self,id):
        #For que percorre as áreas especiais
        for x in range(len(self.areasEspeciais)):
            #Ao invés de excluir perdendo a informação, o metodo seta Inativa na area escolhina na interação
            if id == self.areasEspeciais[x][0]:
                self.areasEspeciais[x][6] = "Inativa"
        return "\nÁrea Especial removida com sucesso!"
    #Retorna a quantidade de vagas por bloco escolhido
    def qntDeVagasPorBloco(self,valor):
        x = 0
        y = ""
        if valor == 1:
            y = "Bloco A"
        elif valor == 2:
            y = "Bloco B"
        elif valor == 3:
            y =" Bloco C"
        elif valor == 4:
            y = "Bloco D"
        elif valor == 5:
            y = "Bloco E"
        elif valor == 6:
            y = "Bloco F"
        elif valor == 7:
            y = "Bloco G"
        elif valor == 8:
            y = "Bloco Central"
        for i in range(len(self.areasEspeciais)):
            if y ==  self.areasEspeciais[i][1]:
                x += int(self.areasEspeciais[i][5])
            elif valor == 0:
                x += int(self.areasEspeciais[i][5])
        return x
    def darPermissao(self,id,acesso):
        temp = ""
        x = ""
        if acesso == 1:
            x = "Funcionário"
        elif acesso == 2:
            x = "Professores"
        elif acesso == 3:
            x = "Convidados"
        elif acesso == 4:
            x = "Reitores"
        elif acesso == 5:
            x = "Outros"
        #For que percorre as áreas especiais
        for i in range(len(self.areasEspeciais)):
            #Ao invés de criar uma outra área para dar uma nova permissão, seta na mesma área o nome do grupo
            #que terá acesso a área escolhida na interação
            if id == self.areasEspeciais[i][0]:
                self.areasEspeciais[i][2] += "/" + x
        return "\nPermissão concebida com sucesso!"
    #Método que verificar se exsite ou não área especial no bloco escolhido na interação
    def verificarAreaEspecial(self,valor):
        temp = ""
        y = ""
        if valor == 1:
            y = "Bloco A"
        elif valor == 2:
            y = "Bloco B"
        elif valor == 3:
            y =" Bloco C"
        elif valor == 4:
            y = "Bloco D"
        elif valor == 5:
            y = "Bloco E"
        elif valor == 6:
            y = "Bloco F"
        elif valor == 7:
            y = "Bloco G"
        elif valor == 8:
            y = "Bloco Central"
        for i in range(len(self.areasEspeciais)):
            if y == self.areasEspeciais[i][1]:
                temp = True
                break
            else:
                temp = False
        return temp
    def gerarRelatorio(self):
        pdf = canvas.Canvas("teste.pdf")
        temp = pdf.beginText(40,680)
        for x in self.areasEspeciais:
            temp.textLine(x)
        pdf.drawString(0,720,"Áreas Especiais")
        pdf.drawText(temp)
        pdf.save()
    def gerarRelatorio(self):
        relatorio = 'RelatorioAreasEspeciais.pdf'
        titulo = [['','','RELATÓRIO','DE','ÁREAS ESPECIAIS','','','']]

        info = [['ID','Bloco','Acesso','Inicio','Fim','Vagas','Status']]
        for i in self.areasEspeciais:
            info.append(i)
        pdf = SimpleDocTemplate(relatorio,pagesize=letter)
        tableTitulo = Table(titulo)
        tableInfo = Table(info)

        styleTitulo = TableStyle([
            ('BACKGROUND',(0,0),(6,0),colors.white),
            ('BOTTOMPADDING',(0,0),(-1,0),12),
            ('FONTSIZE',(0,0),(-1,0),20),
            
        ])
        styleInfo = TableStyle([
            ('TEXTECOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('BACKGROUND',(0,0),(-1,-1),colors.white),
            ('GRID',(0,0),(-1,-1),2,colors.black),
            ('FONTNAME',(0,0),(-1,-1),'Courier'),
            ('FONTNAME',(0,0),(6,0),'Courier-Bold')
        ])
        tableTitulo.setStyle(styleTitulo)
        tableInfo.setStyle(styleInfo)

        vetor = []
        vetor.append(tableTitulo)
        vetor.append(tableInfo)
        pdf.build(vetor)
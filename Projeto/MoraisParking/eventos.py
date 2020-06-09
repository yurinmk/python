from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

class Eventos():
    def __init__(self):
        self.nome = ''
        self.inicio = ''
        self.fim = ''
        self.local = ''
        self.vagas = ''
        self.status = ''
        self.eventos = [
            ['Games Aleatórios', '01/06/2020','30/06/2020','Bloco Central','30','em_andamento'],
            ['Tenda Eletônica', '01/06/2020','16/06/2020','Bloco A','10','em_andamento']
        ]
    def setNome(self,nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    def setInicio(self,inicio):
        self.inicio = inicio
    def getInicio(self):
        return self.inicio
    def setFim(self,fim):
        self.fim = fim
    def getFim(self):
        return self.fim
    def setLocal(self,local):
        self.local = local
    def getLocal(self):
        return self.local
    def setVagas(self,vagas):
        self.vagas = vagas
    def getVagas(self):
        return self.vagas
    def setStatus(self,status):
        self.status = status
    def getStatus(self):
        return self.status
    def cadastrarEventos(self,nome,inicio,fim,local,vagas):
        temp = []
        temp.append(nome)
        temp.append(inicio)
        temp.append(fim)
        if local == 1:
            temp.append("Bloco A")
        elif local == 2:
            temp.append("Bloco B")
        elif local == 3:
            temp.append("Bloco C")
        elif local == 4:
            temp.append("Bloco D")
        elif local == 5:
            temp.append("Bloco E")
        elif local == 6:
            temp.append("Bloco F")
        elif local == 7:
            temp.append("Bloco G")
        elif local == 8:
            temp.append("Bloco Central")
        temp.append(vagas)
        if (datetime.strptime(inicio, "%d/%m/%Y").timestamp()*1000) <= (datetime.strptime(str(datetime.now().date()), "%Y-%m-%d").timestamp()*1000) and \
         (datetime.strptime(str(datetime.now().date()), "%Y-%m-%d").timestamp()*1000) <= (datetime.strptime(fim, "%d/%m/%Y").timestamp()*1000):
            temp.append("em_andamento")
        elif (datetime.strptime(str(datetime.now().date()), "%Y-%m-%d").timestamp()*1000) < (datetime.strptime(inicio, "%d/%m/%Y").timestamp()*1000):
            temp.append("futuro")
        else:
            temp.append("finalizado")
        self.eventos.append(temp)
    def monitorarEventos(self,valor):
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
        if valor == 0:
            for x in range(len(self.eventos)):
                temp += "\n| Nome: " + self.eventos[x][0] + " | Data Inicio: " + self.eventos[x][1] +\
                    " | Data Fim: " + self.eventos[x][2] + " | Local: " + self.eventos[x][3] + \
                        " | QNT Vagas: " + self.eventos[x][4] + " | Status: " + self.eventos[x][5] + " |\n"
        else:
            for x in range(len(self.eventos)):
                if self.eventos[x][3] == y:
                    temp += "\n| Nome: " + self.eventos[x][0] + " | Data Inicio: " + self.eventos[x][1] +\
                        " | Data Fim: " + self.eventos[x][2] + " | Local: " + self.eventos[x][3] + \
                            " | QNT Vagas: " + self.eventos[x][4] + " | Status: " + self.eventos[x][5] + " |\n"
        return temp
    def totalDeVagasPorBloco(self,valor):
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
        for i in range(len(self.eventos)):
            if y == self.eventos[i][3]:
                if self.eventos[i][5] == "em_andamento" or self.eventos[i][5] == "finalizado": 
                    x += int(self.eventos[i][4])
            elif valor == 0:
                if self.eventos[i][5] == "em_andamento" or self.eventos[i][5] == "finalizado": 
                    x += int(self.eventos[i][4])
        return x
    def gerarRelatorio(self):
        relatorio = 'RelatorioEventos.pdf'
        titulo = [['','','RELATÓRIO','DE','EVENTOS','','','']]

        info = [['Nome','Inico','Fim','Bloco','Vagas','Status']]
        for i in self.eventos:
            info.append(i)
        pdf = SimpleDocTemplate(relatorio,pagesize=letter)
        tableTitulo = Table(titulo)
        tableInfo = Table(info)

        styleTitulo = TableStyle([
            ('BACKGROUND',(0,0),(5,0),colors.white),
            ('BOTTOMPADDING',(0,0),(-1,0),12),
            ('FONTSIZE',(0,0),(-1,0),20),
            
        ])
        styleInfo = TableStyle([
            ('TEXTECOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('BACKGROUND',(0,0),(-1,-1),colors.white),
            ('GRID',(0,0),(-1,-1),2,colors.black),
            ('FONTNAME',(0,0),(-1,-1),'Courier'),
            ('FONTNAME',(0,0),(5,0),'Courier-Bold')
        ])
        tableTitulo.setStyle(styleTitulo)
        tableInfo.setStyle(styleInfo)

        vetor = []
        vetor.append(tableTitulo)
        vetor.append(tableInfo)
        pdf.build(vetor)
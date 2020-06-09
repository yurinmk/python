import random
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
class Ocorrencias():
    def __init__(self):
        self.placa = ''
        self.matricula = ''
        self.nome = ''
        self.marca = ''
        self.tipo = ''
        self.ocorrencia = ''
        self.data = ''
        self.local = ''
        self.protocolo = ''
        self.ocorrencia = [['mof6616','1313','Ericleiton','Gol','Carro','Furto ou Assalto','05/04/2020','Bloco A','0.12345']]
    def setPlaca(self,placa):
        self.placa = placa
    def getPlaca(self):
        return self.placa
    def setMatricula(self,matricula):
        self.matricula = matricula
    def getMatricula(self):
        return self.matricula
    def setNome(self,nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    def setMarma(self,marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    def setTipo(self,tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def setOcorrencia(self,ocorrencia):
        self.ocorrencia = ocorrencia
    def getOcorrencia(self):
        return self.ocorrencia
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def setLocal(self,local):
        self.local = local
    def getLocal(self):
        return self.local
    def setProtocolo(self,protocolo):
        self.protocolo = protocolo
    def getProtocolo(self):
        return self.protocolo
    def cadastrarOcorrencia(self,placa,matricula,nome,marca,tipo,valor,data,local):
        temp = []
        y = ""
        if valor == 1:
            y = "Batidas"
        elif valor == 2:
            y = "Furto ou Assalto"
        elif valor == 3:
            y = "Estacionamento Indevido"
        elif valor == 4:
            y = "Inundação"
        elif valor == 5:
            y = "Dano ao Veículo"
        elif valor == 6:
            y = "Outros"
        temp.append(placa)
        temp.append(matricula)
        temp.append(nome)
        temp.append(marca)
        temp.append(tipo)
        temp.append(y)
        temp.append(data)
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
        temp.append(round(10*random.random(),5))
        self.ocorrencia.append(temp)    
    def monitorarOcorrencia(self,valor):
        temp = ''
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
            for x in range(len(self.ocorrencia)):
                temp += "\n| Placa: " + self.ocorrencia[x][0] + " | Matricula: " + self.ocorrencia[x][1] + \
                    " | Nome: " + self.ocorrencia[x][2] + " | Marca: " + self.ocorrencia[x][3] + "| Tipo: " + self.ocorrencia[x][4] \
                        + " | Ocorrência: " + self.ocorrencia[x][5] + " | Data: " + self.ocorrencia[x][6] + " | Local: " + \
                            self.ocorrencia[x][7] + " | Protocolo: " + str(self.ocorrencia[x][8]) + " |"
        else:
            for x in range(len(self.ocorrencia)):
                if self.ocorrencia[x][7] == y:
                    temp += "\n| Placa: " + self.ocorrencia[x][0] + " | Matricula: " + self.ocorrencia[x][1] + \
                        " | Nome: " + self.ocorrencia[x][2] + " | Marca: " + self.ocorrencia[x][3] + "| Tipo: " + self.ocorrencia[x][4] \
                            + " | Ocorrência: " + self.ocorrencia[x][5] + " | Data: " + self.ocorrencia[x][6] + " | Local: " + \
                                self.ocorrencia[x][7] + " | Protocolo: " + str(self.ocorrencia[x][8]) + " |"
        return temp
    def gerarRelatorio(self):
        relatorio = 'RelatorioOcorrencias.pdf'
        titulo = [['','','RELATÓRIO','DE','OCORRÊNCIAS','','','']]

        info = [['Placa','Matricula','Nome','Marca','Tipo','Ocorrência','Data','Bloco','Protocolo']]
        for i in self.ocorrencia:
            info.append(i)
        pdf = SimpleDocTemplate(relatorio,pagesize=letter)
        tableTitulo = Table(titulo)
        tableInfo = Table(info)

        styleTitulo = TableStyle([
            ('BACKGROUND',(0,0),(8,0),colors.white),
            ('BOTTOMPADDING',(0,0),(-1,0),12),
            ('FONTSIZE',(0,0),(-1,0),20),
        ])
        styleInfo = TableStyle([
            ('TEXTECOLOR',(0,0),(-1,0),colors.whitesmoke),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('BACKGROUND',(0,0),(-1,-1),colors.white),
            ('GRID',(0,0),(-1,-1),2,colors.black),
            ('FONTNAME',(0,0),(-1,-1),'Courier'),
            ('FONTNAME',(0,0),(8,0),'Courier-Bold')
        ])
        tableTitulo.setStyle(styleTitulo)
        tableInfo.setStyle(styleInfo)

        vetor = []
        vetor.append(tableTitulo)
        vetor.append(tableInfo)
        pdf.build(vetor)
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
class Veiculo:
    def __init__(self):
        self.matricula = ''
        self.nome= ''
        self.placa = ''
        self.marca= ''
        self.tipo= ''
        self.data = ''
        self.status = ''
        self.bloco = ''
        self.totalVagas = 371
        self.vagasPreenchidas = 0
        self.banco = [['1212','Yuri','nmk0412','Harley Davyson','Moto','04/05/2020','Ausente','Bloco A'],
                      ['1313','Ericleiton','mof6616','Gol','Carro','05/04/2020','Presente','Bloco A'],
                      ['1414','Aline','ali0101','Toro','Carro','01/06/2020','Presente','Bloco Central'],
                      ['1515','Alana','ala0202','XRE','Moto','01/06/2020','Ausente','Bloco Central']]

    def getTotalVagas(self):
        return self.totalVagas
    def getVagasDisponiveis(self):
        return self.totalVagas - self.vagasPreenchidas
    def getVagasPreenchidas(self):
        return self.vagasPreenchidas
    def cadastrarVeiculo(self,matricula,nome,placa,marca,tipo,bloco):
        veiculo = []
        veiculo.append(matricula)
        veiculo.append(nome)
        veiculo.append(placa)
        veiculo.append(marca)
        veiculo.append(tipo)
        veiculo.append((datetime.now().date()).strftime('%d/%m/%Y'))
        veiculo.append('Presente')
        if bloco == 1:
            veiculo.append("Bloco A")
        elif bloco == 2:
            veiculo.append("Bloco B")
        elif bloco == 3:
            veiculo.append("Bloco C")
        elif bloco == 4:
            veiculo.append("Bloco D")
        elif bloco == 5:
            veiculo.append("Bloco E")
        elif bloco == 6:
            veiculo.append("Bloco F")
        elif bloco == 7:
            veiculo.append("Bloco G")
        elif bloco == 8:
            veiculo.append("Bloco Central")
        self.banco.append(veiculo)
    def monitoramentoVeiculos(self,valor,status):
        self.vagasPreenchidas = 0
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
            for x in range(len(self.banco)):
                if status == self.banco[x][6]:
                    temp += "\n| Matrícula: " + self.banco[x][0] + " | Nome:  " + self.banco[x][1] +\
                        " | Placa: " + self.banco[x][2] + " | Marca: " + self.banco[x][3] + \
                            " | Tipo: " + self.banco[x][4] + " | Data: " + str(self.banco[x][5]) +\
                                " | Status: " + self.banco[x][6] +" | Bloco: " + self.banco[x][7] + " |\n"
                    self.vagasPreenchidas += 1

        else:
            for x in range(len(self.banco)):
                if self.banco[x][7] == y and self.banco[x][6] == status:
                    temp += "\n| Matrícula: " + self.banco[x][0] + " | Nome:  " + self.banco[x][1] +\
                        " | Placa: " + self.banco[x][2] + " | Marca: " + self.banco[x][3] + \
                            " | Tipo: " + self.banco[x][4] + " | Data: " + str(self.banco[x][5]) +\
                                " | Status: " + self.banco[x][6] +" | Bloco: " + self.banco[x][7] + " |\n"
                    self.vagasPreenchidas += 1
        return temp
    def pesquisarVeiculo(self,placa,status):
        temp = ''
        for i in range(len(self.banco)):
            if placa==self.banco[i][2] and status ==self.banco[i][6]:
                temp = True
                break
            else:
                temp = False
        return temp
    def inserirEstaciomanento(self,valor,placa):
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
        for i in range(len(self.banco)):
            if placa in self.banco[i]:
                self.banco[i][6] = 'Presente'
                self.banco[i][7] = y
        return 'Veículo inserido com sucesso!'             
    def removerVeiculo(self, placa):
        for i in range(len(self.banco)):
            if placa==self.banco[i][2]:
                self.banco[i][6] = 'Ausente'
        return '\nVeículo removido com sucesso!'
    def pesquisarVeiculoPorData(self,data,status):
        self.vagasPreenchidas = 0
        temp = ""
        for x in range(len(self.banco)):
            if data == self.banco[x][5] and self.banco[x][6] == status:
                temp += "\n| Matrícula: " + self.banco[x][0] + " | Nome:  " + self.banco[x][1] +\
                        " | Placa: " + self.banco[x][2] + " | Marca: " + self.banco[x][3] + \
                            " | Tipo: " + self.banco[x][4] + " | Data: " + self.banco[x][5] +\
                                " | Status: " + self.banco[x][6] +" | Bloco: " + self.banco[x][7] + " |\n"
                self.vagasPreenchidas += 1
        return temp
    def gerarRelatorio(self):
        relatorio = 'RelatorioVeiculo.pdf'
        titulo = [['','','RELATÓRIO','DE','VEÍCULOS','','','']]

        info = [['Matricula','Nome','Placa','Marca','Tipo','Data','Status','Bloco']]
        for i in self.banco:
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
            ('FONTNAME',(0,0),(7,0),'Courier-Bold')
        ])
        tableTitulo.setStyle(styleTitulo)
        tableInfo.setStyle(styleInfo)

        vetor = []
        vetor.append(tableTitulo)
        vetor.append(tableInfo)
        pdf.build(vetor)


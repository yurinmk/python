from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

teste = 'teste.pdf'

titulo = [['','','RELATÓRIO','DE','VEÍCULOS','','','']]

topo = [['Matricula','Nome','Placa','Marca','Tipo','Data','Status','Bloco']]

info = [['1212','Yuri','nmk0412','Harley Davyson','Moto','04/05/2020','Ausente','Bloco A'],
        ['1313','Ericleiton','mof6616','Gol','Carro','05/04/2020','Presente','Bloco A'],
        ['1414','Aline','ali0101','Toro','Carro','01/06/2020','Presente','Bloco Central'],
        ['1515','Alana','ala0202','XRE','Moto','01/06/2020','Ausente','Bloco Central']]
for i in info:
    topo.append(i)

pdf = SimpleDocTemplate(teste,pagesize=letter)
tableTitulo = Table(titulo)
tableTopo = Table(topo)

styleTitulo = TableStyle([
    ('BACKGROUND',(0,0),(8,0),colors.white),
    ('BOTTOMPADDING',(0,0),(-1,0),12),
    ('FONTSIZE',(0,0),(-1,0),20),
    
])
styleTopo = TableStyle([
    ('TEXTECOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('BACKGROUND',(0,0),(-1,-1),colors.white),
    ('GRID',(0,0),(-1,-1),2,colors.black),
    ('FONTNAME',(0,0),(-1,-1),'Courier'),
    ('FONTNAME',(0,0),(7,0),'Courier-Bold')
])
tableTitulo.setStyle(styleTitulo)
tableTopo.setStyle(styleTopo)

vetor = []
vetor.append(tableTitulo)
vetor.append(tableTopo)
pdf.build(vetor)
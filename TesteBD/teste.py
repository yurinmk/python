import pymysql

conexao = pymysql.connect(db='db_morais_parking',user='namikoka',passwd='Y1832902204c')

cursor = conexao.cursor()

cursor.execute("select * from veiculos")

resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

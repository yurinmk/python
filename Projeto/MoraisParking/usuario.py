class Usuario:
    def __init__(self):
        self.nome = ''
        self.senha = ''
        self.cargo = ''
        self.banco = [['yuri','123','gestor'],['ericleiton','123','funcionário'],['aline','123','RH']]
    def cadastrar(self, nome, senha,cargo):
        temp = []
        temp.append(nome)
        temp.append(senha)
        temp.append(cargo)
        self.banco.append(temp)
    def getBanco(self):
         return self.banco
    def verificarUsuario(self,nome,senha,cargo):
        temp = ''
        for i in range(len(self.banco)):
            if self.banco[i][0] == nome and self.banco[i][1] == senha and self.banco[i][2] == cargo: 
                temp = True 
                break 
            else:
                temp = False
        return temp
    def banco(self):
        return self.banco


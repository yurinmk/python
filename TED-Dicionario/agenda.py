class DevedoresBodegaDonaChica:
    def __init__(self):
        self.devedores = {}
        self.nome = ''
        self.valor= ''
        self.fone = ''
        self.cep = ''
        self.numero = ''
        self.rua = ''
    def cadastroDevedor(self,nome,valor,fone,cep,rua,numero):
        self.devedores[nome] = [valor,fone,cep,rua,numero]        
    def pesquisarDevedores(self,nome):
        temp = False
        for c,v in self.devedores.items():
            if nome in c:
                print("\nNome:",c,"\nValor: R$",v[0],"\nTelefone:", v[1],"\nCEP:", v[2]\
                    ,"\nEndereço:", v[3],"\nNúmero:", v[4])
                temp = True
            return temp
    def atualizarDivida(self,nome,valor):
        temp = False
        for c,v in self.devedores.items():
            if nome in c:
                v[0] = valor
                temp = True
        return temp
    def removerDevedor(self,nome):
        temp = False
        if nome in self.devedores.keys():
            del self.devedores[nome]
            temp = True
        return temp
    def mostrarTodosDevedores(self):
        i = 1
        for c,v in self.devedores.items():
            print("\nDevedor",i)
            print("Nome:",c,"\nValor: R$",v[0],"\nTelefone:", v[1],"\nCEP:", v[2]\
                ,"\nEndereço:", v[3],"\nNúmero:", v[4])
            i += 1
from agenda import DevedoresBodegaDonaChica
from interacao import Interacao

def main():
    devedor = DevedoresBodegaDonaChica()
    interacao = Interacao()
    print(interacao.menuPrincipal())
    entrada = int(input("Digite: "))
    while entrada <=5 :
        if entrada == 1:
            print("\nCadastro de Devedores")
            nome = input("Nome: ")
            valor = input("Valor: ")
            fone = input("Telefone: ")
            cep = input("CEP: ")
            rua = input("Endereço: ")
            numero = input("Número: ")
            devedor.cadastroDevedor(nome,valor,fone,cep,rua,numero)
            print("\nCadastro realizado com sucesso!")
        if entrada == 2:
            nome = input("Digite o nome do devedor: ")
            x = devedor.pesquisarDevedores(nome)
            if x == False:
                print("\nNome não localizado!!")
        if entrada == 3:
            print("\nAtualização da dívida")
            nome = input("Digite o nome do devedor: ")
            valor = input("Digite o valor total da nova dívida: ")
            x = devedor.atualizarDivida(nome,valor)
            if(x == True):
                print("\nValor da dívida atualizado!!")
            else:
                print("\nAlgo deu errado, tente novamente!")
        if entrada == 4:
            print("\nRemover devedor")
            nome = input("Digite o nome do antigo devedor: ")
            x = devedor.removerDevedor(nome)
            if x == True:
                print("\nPronto! Quem devia, agora não deve mais!")
            else:
                print("\nAlgo deu errado, tente novamente!")
        if entrada == 5:
            devedor.mostrarTodosDevedores()
        if entrada == 0:
            exit()
        print(interacao.menuPrincipal())
        entrada = int(input("Digite: "))
        
    
  
main()
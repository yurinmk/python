from usuario import Usuario
from interacao import Interacao
from veiculo import Veiculo
from eventos import Eventos
from ocorrencias import Ocorrencias
from areasEspeciais import AreasEspeciais
def main():
    print('Bem vindo ao MoraisParking!')
    #Criação dos objetos
    usuario = Usuario()
    interacao = Interacao()
    veiculo = Veiculo()
    evento = Eventos()
    ocorrencia = Ocorrencias()
    areasE = AreasEspeciais()
    print(interacao.getInteracao())
    entrada = int(input("Digite: "))
    #Caso seja digitada alguma opção inválida
    while entrada > 2:
        print("Opção invalida. Tente novamente!")
        print(interacao.getInteracao())
        entrada = int(input("Digite: "))
    #Tela de iniciação para fazer login    
    while entrada < 3:
        if entrada == 1:
            print("\nRealizar Login")
            print("1 - Funcionário\n2 - RH\n3 - Gestor")
            x = int(input("Digite: "))
            #Realizar login
            if x == 1:
                print("\nTela de Login Funcionário")
                nome = input("Nome: ")
                senha = input("Senha: ")
                cargo = "funcionário"
                #Verificação se existe usuário ou não
                validacao = usuario.verificarUsuario(nome,senha,cargo)
                #Caso a validação dê errado
                while validacao == False:
                        print("\nUsuário ou senha Inválidos!\nTente Novamente.\n")
                        nome = input("Nome: ")
                        senha = input("Senha: ")
                        cargo = "funcionário"
                        validacao = usuario.verificarUsuario(nome,senha,cargo)
            elif x == 2:
                print("\nTela de Login RH")
                nome = input("Nome: ")
                senha = input("Senha: ")
                cargo = "RH"
                #Verificação se existe usuário ou não
                validacao = usuario.verificarUsuario(nome,senha,cargo)
                #Caso a validação dê errado
                while validacao == False:
                        print("\nUsuário ou senha Inválidos!\nTente Novamente.\n")
                        nome = input("Nome: ")
                        senha = input("Senha: ")
                        cargo = "RH"
                        validacao = usuario.verificarUsuario(nome,senha,cargo)
            if x == 3:
                print("\nTela de Login Gestor")
                nome = input("Nome: ")
                senha = input("Senha: ")
                cargo = "gestor"
                #Verificação se existe usuário ou não
                validacao = usuario.verificarUsuario(nome,senha,cargo)
                #Caso a validação dê errado
                while validacao == False:
                        print("\nUsuário ou senha Inválidos!\nTente Novamente.\n")
                        nome = input("Nome: ")
                        senha = input("Senha: ")
                        cargo = "gestor"
                        validacao = usuario.verificarUsuario(nome,senha,cargo)
            #Caso a validação dê certo para funcionário
            if (validacao == True and x == 1):
                print("\nMenu do Funcionário")
                print(interacao.getInteracao2())
                entradaI2 = int(input("Digite: "))
                #Loop da interação
                while entradaI2 < 9:
                    #Interação de cadastrar veículos
                    if entradaI2 == 1:
                        print("\nTela de cadastro de veículos")
                        matricula = input('Insira uma matricula: ')
                        nome = input('Insira um nome: ')
                        placa = input('Insira um placa: ')
                        marca = input('Insira um marca: ')
                        tipo = input('Insira um tipo: ')
                        print("\n"+interacao.getInteracao4())
                        bloco = int(input("Digite: "))
                        veiculo.cadastrarVeiculo(matricula,nome,placa,marca,tipo,bloco)
                        print("\nVeículo cadastrado com sucesso!")
                        print("O que mais deseja fazer?")
                    #Interação de identificar veículos
                    elif entradaI2 == 2:
                        print("\nTela de Identificação do Veículos")
                        placa = input('Digite a placa do veiculo: ')
                        #Só identifica os veículos ausentes
                        status = "Ausente"
                        #verificação se existe ou não o veículos
                        if veiculo.pesquisarVeiculo(placa,status):
                            print("\nEstacionar " + interacao.getInteracao4())
                            bloco = int(input("Digite o bloco para o veículo estacionar: "))
                            print(veiculo.inserirEstaciomanento(bloco,placa))
                        #caso não exista, solicitar o cadastro do mesmo
                        else:
                            #se quer cadastrar ou não
                            rs = input("Deseja cadastrar o Veículo (S/N)?: ")
                            if rs == 'S' or rs == 's':
                                print("\nCadastre o Veículo\n")
                                matricula = input('Insira um matricula: ')
                                nome = input('Insira um nome: ')
                                placa = input('Insira um placa: ')
                                marca = input('Insira um marca: ')
                                tipo = input('Insira um tipo: ')
                                data = input('Insira um data: ')
                                hora = input('Insira um hora: ')
                                bloco = input('Insira um bloco: ')
                                veiculo.cadastrarVeiculo(matricula,nome,placa,marca,tipo,data,hora,bloco)
                                print("Veículo cadastrado com sucesso!")
                                print("O que mais deseja fazer?")
                            #se não quiser cadastrar, o sistema não faz nada
                            else:
                                print()
                    #Interação de remoção de veículos
                    elif entradaI2 == 3:
                        print("\nTela de remoção de veículo")
                        placa = input('Digite a placa do veiculo: ')
                        status = "Presente"
                        #verifica se existe veículo
                        teste = veiculo.pesquisarVeiculo(placa,status)
                        if teste == True:
                            #se existir pergunta se realmente quer remover
                            rs = input('Deseja realmente remover o veículo? (S/N): ')
                            if rs == 'S' or rs == 's':
                                print(veiculo.removerVeiculo(placa))
                        #se não existir, retorna mensagem de erro
                        else:
                            print("Veículo não encontrado!")
                    #Interação de cadastro de eventos
                    elif entradaI2 == 4:
                        print("\nCadastro de Eventos")
                        nome = str(input('Nome: '))
                        inicio = str(input('Data Inicio (dd/MM/yyyy): '))
                        fim = str(input('Data Fim (dd/MM/yyyy): '))
                        print("\n"+interacao.getInteracao4())
                        local = int(input("Digite: "))
                        vagas = str(input('QNT Vagas: '))
                        evento.cadastrarEventos(nome,inicio,fim,local,vagas)
                        print("\nEvento cadastrado com sucesso!")
                        print("O que mais deseja fazer?")
                    #Interação de cadastro de ocorrências
                    elif entradaI2 == 5:
                        print("\nCadastro de Ocorrências")
                        placa = str(input("Placa: "))
                        matricula = str(input("Matricula: "))
                        nome = str(input("Nome: "))
                        marca = str(input("Marca: "))
                        tipo = str(input("Tipo: "))
                        #chama a interação dos tipos de ocorrências
                        print(interacao.getInteracaoOcorrencias())
                        tipoOcorrencia = int(input("Ocorrencia: "))
                        data = str(input("Data (dd/MM/yyyy): "))
                        print("\n"+interacao.getInteracao4())
                        local = int(input("Digite: "))
                        ocorrencia.cadastrarOcorrencia(placa,matricula,nome,marca,tipo,tipoOcorrencia,data,local)
                        print("\nOcorrência cadastrada com sucesso!")
                        print("O que mais deseja fazer?")
                    #Interação de monitoramento do estacionamento                                                     
                    elif entradaI2 == 6:
                        print("\nDigite uma das opções!")
                        print("1 - Ausentes")
                        print("2 - Presentes")
                        x = int(input("Digite: "))
                        #Caso a escolha for ausente
                        if x == 1:
                            print("\nDigite uma das opções!")
                            print("1 - Por Blocos")
                            print("2 - Por Data")
                            c = int(input("Digite: "))
                            #Caso a escolha for por bloco
                            if c == 1:
                                print(interacao.getInteracao3())
                                valor = int(input("Digite: "))
                                print("\nTela de Monitoramento")
                                print(veiculo.monitoramentoVeiculos(valor,"Ausente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis())+ " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas()) +" |")
                            #Caso a escolha for por data
                            elif c == 2:
                                data = input("Digite uma data (dd/MM/yyyy): ")
                                print("\nTela de Monitoramento")
                                print(veiculo.pesquisarVeiculoPorData(data,"Ausente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis()) + " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas()) +" |")
                        #Caso a escolha for presente
                        elif x == 2:
                            print("\nDigite uma das opções!")
                            print("1 - Por Blocos")
                            print("2 - Por Data")
                            c = int(input("Digite: "))
                            #Caso a escolha for por bloco
                            if c == 1:
                                print(interacao.getInteracao3())
                                valor = int(input("Digite: "))
                                print("\nTela de Monitoramento")
                                print(veiculo.monitoramentoVeiculos(valor,"Presente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis()- evento.totalDeVagasPorBloco(valor) - areasE.qntDeVagasPorBloco(valor)) + " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas() + evento.totalDeVagasPorBloco(valor) + areasE.qntDeVagasPorBloco(valor)) +\
                                            " | Vagas reservadas para Eventos: " + str(evento.totalDeVagasPorBloco(valor)) + \
                                                " | Vagas de Áreas Especiais: " + str(areasE.qntDeVagasPorBloco(valor))+" |")
                            #Caso a escolha for por data
                            elif c == 2:
                                data = input("Digite uma data (dd/MM/yyyy): ")
                                print("\nTela de Monitoramento")
                                print(veiculo.pesquisarVeiculoPorData(data,"Presente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis()) + " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas()) +" |") 
                    #Interação de monitoramento de eventos
                    elif entradaI2 == 7:
                        print(interacao.getInteracao3())
                        valor = int(input("Digite: "))
                        print("\nTela de Monitoramento")
                        print(evento.monitorarEventos(valor))
                    #Interação de monitoramento de ocorrências
                    elif entradaI2 == 8:
                        print(interacao.getInteracao3())
                        valor = int(input("Digite: "))
                        print("\nTela de Monitoramento")
                        print(ocorrencia.monitorarOcorrencia(valor))
                    #encerrar o sistema direto sem deslogar
                    elif entradaI2 == 0:
                        print('Volte quando quiser! =)')
                        exit()
                    print("\nMenu do Funcionário")
                    print(interacao.getInteracao2())
                    entradaI2 = int(input("Digite: "))
                if entradaI2 == 100:
                    print("Usuário deslogado!")
            #Caso a validação dê certo para RH
            elif (validacao == True and x == 2):
                print("\nMenu do RH")
                print(interacao.getInteracaoRH())
                entrada = int(input("Digite: "))
                while entrada != 100:
                    #Cadastrar um funcionário
                    if entrada == 1:
                        print("\nCadastre um Funcionário")
                        nome = input("Nome: ")
                        senha = input("Senha: ")
                        cargo = ""
                        print("1 - Funcionário\n2 - RH\n3 - Gestor")
                        x = int(input("Digite: "))
                        if x == 1:
                            cargo = "funcionário"
                        elif x == 2:
                            cargo = "RH"
                        elif x == 3:
                            cargo = "gestor"
                        usuario.cadastrar(nome, senha,cargo)
                        print("\nCadastro realizado com sucesso!")
                        print('O que mais deseja fazer?')
                    #Dar permissão a uma áres especial
                    elif entrada == 2:
                        print("\nDar Permissão "+interacao.getInteracao4())
                        valor = int(input("Digite: "))
                        status = "Ativa"
                        print(areasE.monitoramentoAreasEspeciaisPorBloco(valor, status))
                        #Verificar se existe área especial naquele bloco
                        if areasE.verificarAreaEspecial(valor):
                            id = input("\nDigite a ID da Área Especial: ")
                            print(interacao.getInteracaoAcesso())
                            acesso = int(input("Quem terá acesso? "))
                            print(areasE.darPermissao(id,acesso))
                        else:
                            print("Não existe Área Especial cadastrada nesse bloco")
                    print("\nMenu do RH")
                    print(interacao.getInteracaoRH())
                    entrada = int(input("Digite: "))
                if entrada == 100:
                    print("Usuário deslogado!")  
            #Caso a validação dê certo para GEstor
            elif (validacao == True and x == 3):
                print("\nMenu do Gestor")
                print(interacao.getInteracaoGestor())
                entradaI2 = int(input("Digite: "))
                #Cadastrar áreas especiais
                while entradaI2 < 10:                                                     
                    if entradaI2 == 1:
                        print("\nCadatrar " + interacao.getInteracao4())
                        bloco = int(input("Bloco: "))
                        print("\nQuem terá acesso?")
                        #Interação dos envolvidos que podem ter acessos
                        print(interacao.getInteracaoAcesso())
                        acesso = int(input("Acesso: "))
                        inicio = input("Inicio (dd/MM/yyyy): ")
                        fim = input("Fim (dd/MM/yyyy): ")
                        vagas  = input("Vagas: ")
                        areasE.cadastrarAreaEspecial(bloco,acesso,inicio,fim,vagas)
                        print('\nArea Especial cadastrada com sucesso!')
                        print('O que mais deseja fazer?')
                    #Monitoramento do Estacionamento
                    elif entradaI2 == 2:
                        print("\nDigite uma das opções!")
                        print("1 - Ausentes")
                        print("2 - Presentes")
                        x = int(input("Digite: "))
                        #Caso a escolha for ausente
                        if x == 1:
                            print("\nDigite uma das opções!")
                            print("1 - Por Blocos")
                            print("2 - Por Data")
                            c = int(input("Digite: "))
                            #Caso a escolha for por bloco
                            if c == 1:
                                print(interacao.getInteracao3())
                                valor = int(input("Digite: "))
                                print("\nTela de Monitoramento")
                                print(veiculo.monitoramentoVeiculos(valor,"Ausente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis())+ " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas()) +" |")
                            #Caso a escolha for por data
                            elif c == 2:
                                data = input("Digite uma data (dd/MM/yyyy): ")
                                print("\nTela de Monitoramento")
                                print(veiculo.pesquisarVeiculoPorData(data,"Ausente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis()) + " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas()) +" |")
                        #Caso a escolha for presente
                        elif x == 2:
                            print("\nDigite uma das opções!")
                            print("1 - Por Blocos")
                            print("2 - Por Data")
                            c = int(input("Digite: "))
                            #Caso a escolha for por bloco
                            if c == 1:
                                print(interacao.getInteracao3())
                                valor = int(input("Digite: "))
                                print("\nTela de Monitoramento")
                                print(veiculo.monitoramentoVeiculos(valor,"Presente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis()- evento.totalDeVagasPorBloco(valor) - areasE.qntDeVagasPorBloco(valor)) + " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas() + evento.totalDeVagasPorBloco(valor) + areasE.qntDeVagasPorBloco(valor)) +\
                                            " | Vagas reservadas para Eventos: " + str(evento.totalDeVagasPorBloco(valor)) + \
                                                " | Vagas de Áreas Especiais: " + str(areasE.qntDeVagasPorBloco(valor))+" |")
                            #Caso a escolha for por data
                            elif c == 2:
                                data = input("Digite uma data (dd/MM/yyyy): ")
                                print("\nTela de Monitoramento")
                                print(veiculo.pesquisarVeiculoPorData(data,"Presente"))
                                print("Total de vagas da respectiva área")
                                #Definições das vagas do estacionamento
                                print("| Total: "+str(veiculo.getTotalVagas())+ " | Total Disponível: " \
                                    + str(veiculo.getVagasDisponiveis()) + " | Vagas Preenchidas: " \
                                        + str(veiculo.getVagasPreenchidas()) +" |") 
                    #Monitoramento de Eventos
                    elif entradaI2 == 3:
                        print(interacao.getInteracao3())
                        valor = int(input("Digite: "))
                        print("\nTela de Monitoramento\n")
                        print(evento.monitorarEventos(valor))
                    #Monitoramento de Ocorrências
                    elif entradaI2 == 4:
                        print(interacao.getInteracao3())
                        valor = int(input("Digite: "))
                        print("\nTela de Monitoramento\n")
                        print(ocorrencia.monitorarOcorrencia(valor))
                    #Monitoramento de Áreas Especiais
                    elif entradaI2 == 5:
                        print(interacao.getInteracao3())
                        valor = int(input("Digite: "))
                        status = 'Ativa'
                        print("\nTela de Monitoramento\n")
                        print(areasE.monitoramentoAreasEspeciaisPorBloco(valor,status))
                    #Remover Áreas Especiais
                    elif entradaI2 == 6:
                        #Primeiro mostra as áreas que existem
                        print(areasE.monitoramentoAreasEspeciaisPorBloco(0,"Ativa"))
                        print()
                        id = input("Digite a ID da Área Especial que deseja remover: ")
                        #Depois exclui a área escolhida
                        print(areasE.removerAreaEspecial(id))
                        print('O que mais deseja fazer?')
                    #Cadastrar Eventos
                    elif entradaI2 == 7:
                        print("\nCadastro de Eventos")
                        nome = str(input('Nome: '))
                        inicio = str(input('Data Inicio (dd/MM/yyyy): '))
                        fim = str(input('Data Fim (dd/MM/yyyy): '))
                        print("\n"+interacao.getInteracao4())
                        local = int(input("Digite: "))
                        vagas = str(input('QNT Vagas: '))
                        evento.cadastrarEventos(nome,inicio,fim,local,vagas)
                        print("\nEvento cadastrado com sucesso!")
                        print("O que mais deseja fazer?")
                    #Dar permissão as áreas especiais
                    elif entradaI2 == 8:
                        print("\nDar Permissão "+interacao.getInteracao4())
                        valor = int(input("Digite: "))
                        status = "Ativa"
                        print(areasE.monitoramentoAreasEspeciaisPorBloco(valor, status))
                        #Verifica se existe área no bloco escolhido
                        if areasE.verificarAreaEspecial(valor):
                            id = input("\nDigite a ID da Área Especial: ")
                            print(interacao.getInteracaoAcesso())
                            acesso = int(input("Quem terá acesso? "))
                            print(areasE.darPermissao(id,acesso))
                        else:
                            print("Não existe Área Especial cadastrada nesse bloco")
                    elif entradaI2 == 9:
                        print("\nTela de extração de Relatórios")
                        print("Extrair relatório\n" + interacao.getInteracaoRelatorios())
                        x = int(input("Digite: "))
                        if x == 1:
                            veiculo.gerarRelatorio()
                            print("\nRelatório extraído com sucesso!")
                        elif x == 2:
                            evento.gerarRelatorio()
                            print("\nRelatório extraído com sucesso!")
                        elif x == 3:
                            ocorrencia.gerarRelatorio()
                            print("\nRelatório extraído com sucesso!")
                        elif x == 4:
                            areasE.gerarRelatorio()
                            print("\nRelatório extraído com sucesso!")
                    #Encerra o sistema direto
                    elif entradaI2 == 0:
                        print('Volte quando quiser! =)')
                        exit()
                    print("\nMenu do Gestor")
                    print(interacao.getInteracaoGestor())
                    entradaI2 = int(input("Digite: "))
                    #Desloga o usuário
                    if entradaI2 == 100:
                        print("Usuário deslogado!")
        #Encerra o sistema direto
        elif entrada == 0:
            print('Volte quando quiser! =)')
            exit()
        print(interacao.getInteracao())
        entrada = int(input("Digite: "))
main()
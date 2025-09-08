from grafoInterface import Grafo #importa a classe Grafo da interface
import os #para poder dar clear no terminal

class Grafer(Grafo):

    #codigos de erros convencionados por mim
    #   quando deve ser inteiro: "valueError1"

    #=================================================================#
    #Metodos para utilidades:

    def clear(): #funcao clear() para limpar o terminal

        # For Windows
        if os.name == "nt":
            os.system("cls")
        # For Linux / Mac
        else:
            os.system("clear")

    def inputInt(inputRaw):

        #tenta converter inputRaw em int
        try:
            inputInt = int(inputRaw)

        except ValueError:
            Grafer.clear()
            print("! ERRO ! Insira um numero INTEIRO! >:P\n")
            errorCode = "valueError1"

            #retorna codigo de erro para ser tratado
            return errorCode
        
        #retorna input em int
        return inputInt
    


    #=================================================================#
    #Metodos para Criar Grafos

    def criarGrafoDenso(size):
        grafo = [[0 for _ in range(size)] for _ in range(size)]
        return grafo
    
    def criarGrafoEsparso(size):
        novoGrafoEsparso = {} 
        counter = int(0)

        while counter != size:
            vertice = input(f'\n: Vértice {counter}: ')
            if vertice == "SAIR":
                Grafer.clear()
                print(": Operação Cancelada! ")
                return "SAIR"
            novoGrafoEsparso.update({vertice: []})
            counter = counter +1

        return novoGrafoEsparso

    #=================================================================#
    #Menus para o programa

    #header com instituicao e aluno
    def header():
        print("[ Menu Principal ]\n")
        print(": CS: IESB ")
        print(": Atividades de Grafos ")
        print(": Aluno: Vitor Hugo Campos ")
        print(": Matricula: 2312130182 \n")

    #menu que mostra os grafos ja criados
    def menuGrafosJaCriados(listaDeGrafos): #quando estiver pronto, implementar tambem em adicionar aresta
        
        print("[ Menu de Grafos já criados ]\n")

        print(f": Numero de Grafos em memória: {len(listaDeGrafos)}\n")

        Grafer.imprimir(listaDeGrafos)
     
        input("\n: Pressione Enter para retornar para o menu pricipal: [ENTER]")
        return

    #menu para realizar a criacao de um novo grafo
    def menuCriaGrafo(listaDeGrafos):
        while True: #primeiro loop do usuario
            value = int(0)
            print("[ Menu de Criação de Grafo ]\n")
            print("  ( 0 ) Retornar para o Menu Principal")
            print("  ( 1 ) Grafo Denso;")
            print("  ( 2 ) Grafo Esparso.\n")

            value = input(": Selecione o tipo do grafo a ser criado: .: ")
            
            #checa se inteiro
            value = Grafer.inputInt(value)
            
            if value != "valueError1":

                #retorna para o menu
                if value == 0: 
                    Grafer.clear()
                    break

                #comeca criacao de grafo denso
                elif value == 1: 
                    while True: #Segundo loop do usuario
                        print("\n: Insira quantos vertices o Grafo Denso deverá ter:")
                        size = input(": Para cancelar a operação digite SAIR e pressione ENTER;\n\n.: ")

                        if size != "SAIR":
                        #confere se input é inteiro e retorna ou errorCode ou o valor em int
                            size = Grafer.inputInt(size)
                            
                            if size != "valueError1":
                                if size <= 16 and size >= 0: #checa se é numero natural e menor q 16
                                    
                                    #cria o grafo e da append na lista de grafos geral
                                    listaDeGrafos.append(Grafer.criarGrafoDenso(size))

                                    Grafer.clear()
                                    print(": Grafo Denso criado!")
                                    print(": Confira ele no menu de grafos ja criados!\n")
                                    break
                                
                                elif size > 16:
                                    Grafer.clear()
                                    print(": Por Favor, escolha uma quantia de vértices menor que 16.")

                                else:
                                    Grafer.clear()
                                    print("!ERRO! Insira um numero MAIOR QUE ZERO! >:P\n")
                        else:
                            Grafer.clear()
                            print(": Operação cancelada!\n")
                            break


                #comeca criacao de grafo esparso
                elif value == 2:
                    while True: #Segundo loop do usuario

                        print("\n: Insira quantos vertices o Grafo Esparso deverá ter:")
                        size = input(": Para cancelar a operação digite SAIR e pressione ENTER;\n\n.: ")
                        if size != "SAIR":
                            size = Grafer.inputInt(size)

                            if size != "valueError1":  
                                if size >= 0 and size <= 16: #checa se é numero natural
                                    print('\n: Agora insira um nome para cada vertice do novo Grafo Esparso:')
                                    print(f': Numero de vertices a serem criados: {size}')
                                    print("\n: Para cancelar a operação digite SAIR e pressione ENTER.\n ")
                                    vertices = (Grafer.criarGrafoEsparso(size))
                                    if vertices != "SAIR":
                                        listaDeGrafos.append(vertices)
                                    else:
                                        break
                                    Grafer.clear()
                                    print(": Grafo Esparso criado!")
                                    print(": Confira ele no menu de grafos já criados!\n")
                                    break

                                elif size > 16:
                                    Grafer.clear()
                                    print(": Por Favor, escolha uma quantia de vertices menor que 16.")
                                else:
                                    Grafer.clear()
                                    print("!ERRO! Insira um numero MAIOR QUE ZERO! >:P\n")
                        else:
                            Grafer.clear()
                            print(": Operação cancelada!\n")
                            break

                #confere se maior q zero
                elif value < 0 or value > 2:
                    Grafer.clear()
                    print(" !ERRO! Insira uma opcao valida >:P\n")
    
    #menu para adicionar aresta
    def menuAdicionaAresta(listaDeGrafos):
        while True: #primeiro loop do usuario
            value = int(0)
            print("[ Menu de Adição e Remoção de Arestas ]\n")
            print("  ( 0 ) Retornar para o Menu Principal")
            print("  ( 1 ) Adicionar Aresta;")
            print("  ( 2 ) Remover Aresta;\n")

            value = input(".: ")
            
            #checa se inteiro
            value = Grafer.inputInt(value)
            
            if value != "valueError1":

                #retorna para o menu
                if value == 0: 
                    Grafer.clear()
                    break

                if value >2 or value < 0:
                    Grafer.clear()
                    print("!ERRO! Insira um numero valido! >:P\n")
                
                #comeca remocao de aresta
                elif value == 2: 
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Menu Remover Arestas ]\n")
                        
                        Grafer.imprimir(listaDeGrafos)

                        print(": Insira o grafo a ser alterado:")
                        indexGrafo = input(": Para cancelar a operação digite SAIR e pressione ENTER;\n\n.: ")
                        Grafer.clear()

                        if indexGrafo == "SAIR":
                            Grafer.clear()
                            print(": Remocao de aresta finalizada!\n")
                            break

                        elif indexGrafo != "SAIR":
                            indexGrafo = Grafer.inputInt(indexGrafo)
                            
                            if indexGrafo != "valueError1": #checa se int

                                #checa se esta no escopo da listaDEGrafos
                                if indexGrafo >= 0 and indexGrafo < len(listaDeGrafos):
                                    while True: #Terceiro loop do usuario

                                        #==================[ Remover EM GRAFO DENSO ]========================================#
                                        #checa se grafo no indice é uma lista
                                        if isinstance(listaDeGrafos[indexGrafo], list):

                                                print(f"[ Remover Aresta no Grafo {indexGrafo} ]\n")
                                                
                                                #printa o grafo pro usuario
                                                print(f"  Grafo {indexGrafo}:  ", end="")
                                                for x in range(len(listaDeGrafos[indexGrafo])): #printa vertices em cima
                                                    print(f"V{x} ", end="")
                                                print("")
                                                for j in range(len(listaDeGrafos[indexGrafo])): #printa vertices na esquerda
                                                    print (f"       V{j}: ",listaDeGrafos[indexGrafo][j])
                                                print("")
                                                
                                                print("!Aviso! Insira apenas o numero do Vertice desejado e pressione ENTER!")
                                                print(": Para finalizar a operação digite SAIR e pressione ENTER;\n")
                                                V1 = input(": Escolha o primeiro vertice: .: ")
                                                if V1 == "SAIR":
                                                    Grafer.clear()
                                                    print(": Remocao de aresta finalizada!\n")
                                                    break
                                                V1 = Grafer.inputInt(V1)

                                                if V1 != "valueError1" and V1 < len(listaDeGrafos[indexGrafo]) and V1 >= 0:
                                                    if V1 >= 0 and V1 <= len(listaDeGrafos[indexGrafo]): #caso input valido
                                                        V2 = input(": Escolha o segundo vertice para remover a aresta: .: ")
                                                        V2 = Grafer.inputInt(V2)
                                                        if V2 != "valueError1":
                                                            if V2 >= 0 and V2 <= len(listaDeGrafos[indexGrafo]): #caso input valido
                                                                print("")

                                                                listaDeGrafos[indexGrafo][V1][V2] = 0

                                                                Grafer.clear()
                                                                print(f": Aresta entre V{V1} e V{V2} Removida!\n")
                                                                

                                                            else:
                                                                Grafer.clear()
                                                                print("!ERRO! Insira um vertice valido >:p\n")
                                                else:
                                                    Grafer.clear()
                                                    print("!ERRO! Insira um vertice valido >:p\n")

                                        #==================[ ADICAO EM GRAFO ESPARSO ]========================================#
                                        #checa se dict
                                        if isinstance(listaDeGrafos[indexGrafo], dict):

                                                print(f"[ Remover Aresta no Grafo {indexGrafo} ]\n")
                                                
                                                #printa o grafo pro usuario
                                                print(f"  Grafo {indexGrafo}:  ")
                                                for y in listaDeGrafos[indexGrafo]:
                                                    print(f"        {y}: {listaDeGrafos[indexGrafo][y]}")
                                                print("")

                                                print("!Aviso! Insira apenas o nome do Vertice desejado e pressione ENTER!")
                                                print(": Para finalizar a operação digite SAIR e pressione ENTER;\n")
                                                V1 = input(": Escolha o primeiro vertice: .: ")
                                                if V1 == "SAIR":
                                                    Grafer.clear()
                                                    print(": Remocao de aresta finalizada!")
                                                    break

                                                if V1 in listaDeGrafos[indexGrafo]:
                                                    V2 = input(": Escolha o segundo vertice para remover a aresta: .: ")

                                                    if V2 in listaDeGrafos[indexGrafo]:
                                                        if V2  in listaDeGrafos[indexGrafo][V1]:
                                                            
                                                            listaDeGrafos[indexGrafo][V1].remove(V2)

                                                            Grafer.clear()
                                                            print(f": Aresta entre {V1} e {V2} adicionada!\n")

                                                        else:
                                                            Grafer.clear()
                                                            print("!ERRO! Essa aresta nao existe >:p\n")
                                                    else:
                                                        Grafer.clear()
                                                        print("!ERRO! Esse Vertice nao existe >:p\n")


                                                else:
                                                    Grafer.clear()
                                                    print("!ERRO! Esse Vertice nao existe >:p\n")
                                        #=======[ FIM ADD ARESTA ESPARSO ]===============================   


                                else:
                                    Grafer.clear()
                                    print("!ERRO! Insira um Grafo valido >:p\n")
                    
                #comeca adicao de aresta
                elif value == 1: 
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Menu Adicao de Arestas ]\n")
                        
                        Grafer.imprimir(listaDeGrafos)

                        print(": Insira o grafo a ser alterado:")
                        indexGrafo = input(": Para cancelar a operação digite SAIR e pressione ENTER;\n\n.: ")
                        Grafer.clear()
                        
                        if indexGrafo == "SAIR":
                            Grafer.clear()
                            print(": Adição de aresta finalizada!")
                            break
                        elif indexGrafo != "SAIR":
                            indexGrafo = Grafer.inputInt(indexGrafo)
                            
                            if indexGrafo != "valueError1": #checa se int

                                #checa se esta no escopo da listaDEGrafos
                                if indexGrafo >= 0 and indexGrafo < len(listaDeGrafos):
                                    while True: #Terceiro loop do usuario

                                        #==================[ ADICAO EM GRAFO DENSO ]========================================#
                                        #checa se grafo no indice é uma lista
                                        if isinstance(listaDeGrafos[indexGrafo], list):

                                                print(f"[ Adicionar Aresta no Grafo {indexGrafo} ]\n")
                                                
                                                #printa o grafo pro usuario
                                                print(f"  Grafo {indexGrafo}:  ", end="")
                                                for x in range(len(listaDeGrafos[indexGrafo])): #printa vertices em cima
                                                    print(f"V{x} ", end="")
                                                print("")
                                                for j in range(len(listaDeGrafos[indexGrafo])): #printa vertices na esquerda
                                                    print (f"       V{j}: ",listaDeGrafos[indexGrafo][j])
                                                print("")
                                                
                                                print("!Aviso! Insira apenas o numero do Vertice desejado e pressione ENTER!")
                                                print(": Para finalizar a operação digite SAIR e pressione ENTER;\n")
                                                V1 = input(": Escolha o primeiro vertice: .: ")
                                                if V1 == "SAIR":
                                                    Grafer.clear()
                                                    print(": Adição de aresta finalizada!\n")
                                                    break
                                                V1 = Grafer.inputInt(V1)

                                                if V1 != "valueError1" and V1 < len(listaDeGrafos[indexGrafo]) and V1 >= 0:
                                                    if V1 >= 0 and V1 <= len(listaDeGrafos[indexGrafo]): #caso input valido
                                                        V2 = input(": Escolha o segundo vertice para realizar a aresta: .: ")
                                                        V2 = Grafer.inputInt(V2)
                                                        if V2 != "valueError1":
                                                            if V2 >= 0 and V2 <= len(listaDeGrafos[indexGrafo]): #caso input valido
                                                                print("")

                                                                listaDeGrafos[indexGrafo][V1][V2] = 1

                                                                Grafer.clear()
                                                                print(f": Aresta entre V{V1} e V{V2} adicionada!\n")
                                                                

                                                            else:
                                                                Grafer.clear()
                                                                print("!ERRO! Insira um vertice valido >:p\n")
                                                else:
                                                    Grafer.clear()
                                                    print("!ERRO! Insira um vertice valido >:p\n")

                                        #==================[ ADICAO EM GRAFO ESPARSO ]========================================#
                                        #checa se dict
                                        if isinstance(listaDeGrafos[indexGrafo], dict):

                                                print(f"[ Adicionar Aresta no Grafo {indexGrafo} ]\n")
                                                
                                                #printa o grafo pro usuario
                                                print(f"  Grafo {indexGrafo}:  ")
                                                for y in listaDeGrafos[indexGrafo]:
                                                    print(f"        {y}: {listaDeGrafos[indexGrafo][y]}")
                                                print("")

                                                print("!Aviso! Insira apenas o nome do Vertice desejado e pressione ENTER!")
                                                print(": Para finalizar a operação digite SAIR e pressione ENTER;\n")
                                                V1 = input(": Escolha o primeiro vertice: .: ")
                                                if V1 == "SAIR":
                                                    Grafer.clear()
                                                    print(": Adição de aresta finalizada!")
                                                    break

                                                if V1 in listaDeGrafos[indexGrafo]:
                                                    V2 = input(": Escolha o segundo vertice para realizar a aresta: .: ")

                                                    if V2 in listaDeGrafos[indexGrafo]:
                                                        if V2 not in listaDeGrafos[indexGrafo][V1]:
                                                            
                                                            listaDeGrafos[indexGrafo][V1].append(V2)

                                                            Grafer.clear()
                                                            print(f": Aresta entre {V1} e {V2} adicionada!\n")

                                                        else:
                                                            Grafer.clear()
                                                            print("!ERRO! Essa aresta ja existe >:p\n")
                                                    else:
                                                        Grafer.clear()
                                                        print("!ERRO! Esse Vertice nao existe >:p\n")


                                                else:
                                                    Grafer.clear()
                                                    print("!ERRO! Esse Vertice nao existe >:p\n")
                                        #=======[ FIM ADD ARESTA ESPARSO ]===============================   


                                else:
                                    Grafer.clear()
                                    print("!ERRO! Insira um Grafo valido >:p\n")

    def menuFuncoes(listaDeGrafos):
        while True: #primeiro loop do usuario
            value = int(0)
            print("[ Menu de Funções entre Grafos ]\n")
            print("  ( 0 ) Retornar para o Menu Principal")
            print("  ( 1 ) Atividade 4")
            print("  ( 1 ) Atividade 5")
            print("  ( 1 ) Atividade 6")
            print("  ( 1 ) Atividade 7")
            print("  ( 1 ) Atividade 9")
            print("  ( 2 ) Grafo Esparso.\n")

            value = input(": Selecione o tipo do grafo a ser criado: .: ")
            
            #checa se inteiro
            value = Grafer.inputInt(value)
            
            if value != "valueError1":

                #retorna para o menu
                if value == 0: 
                    Grafer.clear()
                    break
                #limite de menus
                if value >2 or value < 0:
                    Grafer.clear()
                    print("!ERRO! Insira um numero valido! >:P\n")
                
                #=================[ Atividade 4 ]======================
                elif value == 1: 
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Atividade 4 ]\n")
                        print("  ( 0 ) Retornar para o Menu Principal")
                        print("  ( 1 ) numero_de_vertices")
                        print("  ( 2 ) numero_de_arestas")
                        print("  ( 3 ) sequencia_de_graus")
                        print("  ( 4 ) adicionar_aresta")
                        print("  ( 5 ) remover_aresta")
                        #checa se inteiro
                        select = input(": Selecione a atividade: .: ")
                        select = Grafer.inputInt(select)

                        #retorna para menu anterior
                        if select != "valueError1":
                            if select == 0:
                                Grafer.clear()
                                break
                            #limite de opcoes
                            if select >5 or select < 0:
                                Grafer.clear()
                                print("!ERRO! Insira um numero valido! >:P\n")
                            
                            #numero de vertices
                            elif select == 1:
                                print(": Escolha o grafo;")
                                print(f": Grafos disponiveis: de 0 a {len(listaDeGrafos)}")
                                grafoEscolha = input("  .: ")
                                grafoEscolha = Grafer.inputInt(grafoEscolha)
                                Grafer.numero_de_vertices(listaDeGrafos, grafoEscolha)

                            #numero de arestas
                            elif select == 2:
                                print(": Escolha o grafo;")
                                print(f": Grafos disponiveis: de 0 a {len(listaDeGrafos)}")
                                grafoEscolha = input("  .: ")
                                grafoEscolha = Grafer.inputInt(grafoEscolha)
                                Grafer.numero_de_arestas(listaDeGrafos, grafoEscolha)
                
                            #sequencia de graus
                            elif select == 3:
                                print(": Escolha o grafo;")
                                print(f": Grafos disponiveis: de 0 a {len(listaDeGrafos)-1}")
                                grafoEscolha = input("  .: ")
                                grafoEscolha = Grafer.inputInt(grafoEscolha)
                                Grafer.sequencia_de_graus(listaDeGrafos, grafoEscolha)
            
                
                #=================[ Atividade 5 ]======================
                elif value == 2: 
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Atividade 5 ]\n")
                        print("  ( 0 ) Retornar para o Menu Principal")
                        print("  ( 1 ) is_simples")
                        print("  ( 2 ) is_nulo")
                        print("  ( 3 ) is_completo")
                        #checa se inteiro
                        select = input(": Selecione a atividade: .: ")
                        select = Grafer.inputInt(select)

                        #retorna para menu anterior
                        if select != "valueError1":
                            if select == 0:
                                Grafer.clear()
                                break
                            #limite de opcoes
                            if select >5 or select < 0:
                                Grafer.clear()
                                print("!ERRO! Insira um numero valido! >:P\n")
                            
                            #is simples
                            elif select == 1:
                                print("")

                #=================[ Atividade 6 ]======================
                elif value == 3: 
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Atividade 6 ]\n")
                        print("  ( 0 ) Retornar para o Menu Principal")
                        print("  ( 1 ) get_vertices")
                        print("  ( 2 ) get_arestas")
                        print("  ( 3 ) is_subgrafo")
                        print("  ( 4 ) is_subgrafo_gerador")
                        print("  ( 5 ) is_subgrafo_induzido")
                        #checa se inteiro
                        select = input(": Selecione a atividade: .: ")
                        select = Grafer.inputInt(select)

                        #retorna para menu anterior
                        if select != "valueError1":
                            if select == 0:
                                Grafer.clear()
                                break
                            #limite de opcoes
                            if select >5 or select < 0:
                                Grafer.clear()
                                print("!ERRO! Insira um numero valido! >:P\n")
                            
                            #numero de vertices
                            elif select == 1:
                                print("")

                #=================[ Atividade 7 ]======================
                elif value == 4: 
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Atividade 7 ]\n")
                        print("  ( 0 ) Retornar para o Menu Principal")
                        print("  ( 1 ) is_isomorfo")
                        #checa se inteiro
                        select = input(": Selecione a atividade: .: ")
                        select = Grafer.inputInt(select)

                        #retorna para menu anterior
                        if select != "valueError1":
                            if select == 0:
                                Grafer.clear()
                                break
                            #limite de opcoes
                            if select >5 or select < 0:
                                Grafer.clear()
                                print("!ERRO! Insira um numero valido! >:P\n")
                            
                            #numero de vertices
                            elif select == 1:
                                print("")

                #=================[ Atividade 9 ]======================
                elif value == 5: 
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Atividade 9 ]\n")
                        print("  ( 0 ) Retornar para o Menu Principal")
                        print("  ( 1 ) numero_de_vertices")
                        print("  ( 2 ) numero_de_arestas")
                        print("  ( 3 ) sequencia_de_graus")
                        print("  ( 4 ) adicionar_aresta")
                        print("  ( 5 ) remover_aresta")
                        #checa se inteiro
                        select = input(": Selecione a atividade: .: ")
                        select = Grafer.inputInt(select)

                        #retorna para menu anterior
                        if select != "valueError1":
                            if select == 0:
                                Grafer.clear()
                                break
                            #limite de opcoes
                            if select >5 or select < 0:
                                Grafer.clear()
                                print("!ERRO! Insira um numero valido! >:P\n")
                            
                            #numero de vertices
                            elif select == 1:
                                print("")

                elif value == 6:
                    Grafer.clear()
                    while True: #Segundo loop do usuario
                        
                        print("[ Menu Especifico para Atividades ]\n")

    #Menu principal porem com outro nome por que sim (preguica de mudar o nome p principal)
    def menuIntro(listaDeGrafos):
        Grafer.clear()

        while True:

            select = int(0)

            #Grafer.clear() deve ser usado no final antes da mensagem de erro
            Grafer.header()

            print(": Bem vindo ao Programa de Manipulação de Grafos!")
            print(": Menus:\n")        
            print(f"  ( 1 ) Grafos já criados: {len(listaDeGrafos)} Grafos Criados;") 
            print("  ( 2 ) Criar novo Grafo;")
            print("  ( 3 ) Adicionar Arestas a um Grafo;")
            print("  ( 4 ) Funções entre Grafos [ Atividades ];")
            print("  ( 0 ) Sair do programa.")
            userIn = input("\n: Insira o numero do menu desejado: .: ")
            
            select = Grafer.inputInt(userIn)

            if select != "valueError1":
                if select <= 4 and select >= 0:
                    break
                else:
                    Grafer.clear()
                    print(" !ERRO! Selecione entre os menus DISPONIVEIS! >:P\n")

        Grafer.clear()
        
        #retorna o numero do menu a ser acessado
        return select
           

    #menu que se comporta como uma funcao main
    def menuMaster ():

        listaDeGrafos = [] #Lista de Grafos deve ser criada em memoria no inico do programa
        g0 = [[0 for _ in range(3)] for _ in range(3)]
        for i in range (len(g0)):
            g0[i][i] = 1        
        g1 = {'a':['b','c'], 'b': ['c'], 'c': ['a']}
        g2 = {1: [2, 3], 2: [1], 3: [2]}
        listaDeGrafos.append(g0)
        listaDeGrafos.append(g1)
        listaDeGrafos.append(g2)

        while True:

            #chama o menu principal e retorna um inteiro para acessar os outros menus
            select = Grafer.menuIntro(listaDeGrafos) 

            #menu de grafos em memoria       
            if select == 1:
                Grafer.menuGrafosJaCriados(listaDeGrafos)
            
            #menu de criar grafo
            elif select == 2:
                Grafer.menuCriaGrafo(listaDeGrafos)

            #menu de eh hmmm
            elif select == 3:
                Grafer.menuAdicionaAresta(listaDeGrafos)
                
            #menu funcoes e atividades
            elif select == 4:
                Grafer.menuFuncoes(listaDeGrafos)

            #sair do programa
            elif select == 0:
                print("! AVISO !\n: Você está prestes a fechar o programa!")
                print(": Todo o progresso realizado será perdido caso você prossiga.")
                print(": Você tem certeza de que deseja fechar o programa?\n")
                areUsure = input('  ( 0 ) Não (retorna ao menu principal)\n  ( 1 ) Sim (termina o programa)\n\n .: ')
                if areUsure == '1': # I had a pretty interesting day !
                    Grafer.clear()
                    print(": Programa terminado com sucesso!\n: Goodbye World!")
                    break

    
    #=================================================================#
    #----------------------------------------------------------#
    #Atividade 4:

    def numero_de_vertices(grafo, index):
        Grafer.clear()
        print(f": Grafo {index} possui {len(grafo[index])} vertices.\n")            
    
    def numero_de_arestas(grafo, index):
        if isinstance(grafo[index], list):#caso list
            counter = int(0)
            for i in range(len(grafo[index])):
                for j in range(len(grafo[index][i])):
                    if grafo[index][i][j] == 1:
                        counter = counter + 1
            Grafer.clear()
            print(f": Grafo {index} possui {counter} arestas.\n") #retorna o numero de arestas

        elif isinstance(grafo[index], dict):#caso dict
            numItems = int(0)
            sumNumItens = int(0)
            for i in grafo[index]:
                numItems = len(grafo[index][i])
                sumNumItens = sumNumItens + numItems
            Grafer.clear()
            print(f": Grafo {index} possui {sumNumItens} arestas.\n") #retorna o numero de arestas

    def sequencia_de_graus(grafo, index):

        graus = [] 
        counter = int(0)
        counter2 = int(0)

        for i in range(len(grafo[index])):
            for j in range(len(grafo[index][i])):
                if grafo[index][i][j] == 1:
                    counter = counter + 1
            graus[counter2] = counter
            counter = 0
            counter2 = counter2 + 1

        return print(graus) #retorna a sequencia de graus
    
    def adicionar_aresta(grafo, u, v):

        grafo[u][v] = 1
        grafo[v][u] = 1

        return print(f"Aresta adicionada entre {Grafer.dict(u)} e {Grafer.dict(v)}.")

    def remover_aresta(grafo, u, v):

        grafo[u][v] = 0
        grafo[v][u] = 0

        return print(f"Aresta removida entre {Grafer.dict(u)} e {Grafer.dict(v)}.")
    
    def sequencia_de_grafos():
        return print("")

    def imprimir(listaDeGrafos):

        for i in range(len(listaDeGrafos)): #print grafo novo a ser implementado
            print(f"  Grafo {i}:  ", end="")

            #caso de print se for lista / esse bloco printa uma lista inteira com formatacao maneira
            if isinstance(listaDeGrafos[i], list):  
                for x in range(len(listaDeGrafos[i])): #printa vertices em cima
                    print(f"V{x} ", end="")
                print("")
                for j in range(len(listaDeGrafos[i])): #printa vertices na esquerda
                    print (f"       V{j}: ",listaDeGrafos[i][j])
                print("")

            #caso de print se for dict / esse bloco printa um dict inteiro com formatacao maneira
            elif isinstance(listaDeGrafos[i], dict):
                print("")
                for y in listaDeGrafos[i]:
                    print(f"        {y}: {listaDeGrafos[i][y]}")
                print("")

    #----------------------------------------------------------#
    #Atividade 5 - Grafo Simples - Nulo - Completo

    def is_simples(self):
    #Um grafo simples NAO possui loops e nao possui mais de uma aresta entre dois vertices
    #Assim, deve-se checar duas condicoes, se ele possui loops e se possui mais de uma aresta
    #entre dois vertices

        for i in range(len (self)):
            if self[i][i] == 1:
                print(f"O grafo não é simples por conta do loop no vertice: {Grafer.dict(i)}")
                return 0
            
        print("O grafo é simples.")
        return 1
            #como o grafo esta em forma de matriz, ele não suporta mais de uma aresta entre dois
            #vertices, mas caso ele suportasse, teria que percorrer cada vertice e checar se ele
            #repete mais de uma vez arestas com um outro vertice

    def is_nulo(self):
    #Um grafo nulo é aquele que possui vertices mas nao ha nenhuma aresta
    #Logo, deve-se percorrer a matriz checando se ha alguma aresta
    #Vale detalhar-se que um grafo nulo pode ser um grafo simples
        for i in range(len(self)):
            for j in range(len(self[i])):
                if self[i][j] == 1:
                    print(f"O grafo não é nulo pois há uma aresta entre {Grafer.dict(i)} e {Grafer.dict(j)}.")
                    return
                
        print("O grafo é nulo.")
        return
    
    def is_completo(self):
    #Um grafo completo é um grafo simples em que todo vértice é adjacente a todos os outros vértices.
    #assim, deve-se primeiro ver se ele é simples para depois ver se ele possui algum vertice que não
    #se conecta com o restantes dos vertices
       
        seGrafoSimples = int(Grafer.is_simples(self))
        if seGrafoSimples == 0:
            print("O grafo não é completo pois ele não é simples.")

        for i in range (len(self)):
            for j in range(len(self[i])):
                if self[i][j] == 0 and i != j:
                    print(f"O grafo não é completo pois o vertice {Grafer.dict(i)} não faz aresta com {Grafer.dict(j)}.")
                    return
                
        print("O grafo é completo.")
        return 
    
    #----------------------------------------------------------#
    #Atividade 6: Subgrafos

    def get_vertices(self):
        verticesDoGrafo = []
        for i in self:
            verticesDoGrafo.append(i)
        return verticesDoGrafo
    
    def get_arestas(self):
        arestasDoGrafo = []
        for i in self:
            arestasDoGrafo.append(self[i])
        return arestasDoGrafo
    
    def is_subgrafo(subGrafo, grafo):
    #um subgrafo é um grafo que pode ser formado com os vertices de um grafo maior,
    #assim como todas as arestas
    #logo, cada vertice de um subgrafo deve existir no grafo maior
        
        for i in subGrafo:
            if i not in grafo:
                print("Nao é subgrafo")
                return 
        return
    
    def is_subgrafo_gerador(self):
        return
    
    def is_subgrafo_induzido(self):
        return

from grafoInterface import Grafo #importa a classe Grafo da interface
import os #para poder dar clear no terminal

class Grafer(Grafo):

    def clear(): #funcao clear() para limpar o terminal

        # For Windows
        if os.name == "nt":
            os.system("cls")
        # For Linux / Mac
        else:
            os.system("clear")

    #=================================================================#
    #Metodos para Criar Grafos

    def criarGrafoDenso(size):
        grafo = [[0 for _ in range(size)] for _ in range(size)]
        return grafo
    
    def criarGrafoEsparso(size):
        return super().criarGrafoEsparso()

    #=================================================================#
    #Menus para o programa

    #header com instituicao e aluno
    def header():
        print(": CS: IESB ")
        print(": Atividades de Grafos ")
        print(": Aluno: Vitor Hugo Campos ")
        print(": Matricula: 2312130182 \n")

    #Menu principal porem com outro nome por que sim (preguica de mudar o nome p principal)
    def menuIntro(listaDeGrafos):
        Grafer.clear()

        while True:

            select = int(0)

            #Grafer.clear() deve ser usado no final antes da mensagem de erro
            Grafer.header()

            print(": Bem vindo ao Programa de Manipulação de Grafos!")
            print(": Menus:\n")        
            print(f"  ( 1 ) Grafos já criados: {len(listaDeGrafos)} Grafos Criados") 
            print("  ( 2 ) Criar novo Grafo;")
            print("  ( 3 ) Adicionar Arestas a um Grafo;")
            print("  ( 4 ) Funções entre Grafos;")
            userIn = input("\n: Selecione o numero do menu desejado: .: ")
            
            try:
                select = int(userIn)
                if select <= 4 and select >= 1:
                    break
                else:
                    Grafer.clear()
                    print(" !ERRO! Selecione entre os menus DISPONIVEIS! >:P\n")

            except ValueError:
                Grafer.clear()
                print(" !ERRO! Selecione um NÚMERO valido! >:P\n")

        Grafer.clear()
        return select
            #retorna o numero do menu a ser acessado

    #menu que mostra os grafos ja criados
    def menuGrafosJaCriados(listaDeGrafos):

        Grafer.header()
        
        print(": Menu de Grafos já criados")

        print(f": Numero de Grafos em memória: {len(listaDeGrafos)}\n")
        for i in range(len(listaDeGrafos)):
            print(f"  Grafo {i}: {listaDeGrafos[i]}")
        input("\n: Pressione Enter para retornar para o menu pricipal: [ENTER]")
        return

    #menu para escolher as funcoes realizadas nas atividades
    def menuFuctionsEntreGrafos(self):

        return super().menuFuctionsEntreGrafos()

    #menu para realizar a criacao de um novo grafo
    def menuCriaGrafo(listaDeGrafos):
        while True: #primeiro loop do usuario
            value = int(0)
            print(": Menu de Criação de Grafo:\n")
            print("  ( 0 ) Retornar para o Menu Principal")
            print("  ( 1 ) Grafo Denso;")
            print("  ( 2 ) Grafo Esparso.\n")

            value = input(": Selecione o tipo do grafo a ser criado: .: ")
            
            try: #verifica input para filtrar strings
                value = int(value)

            except ValueError:
                Grafer.clear()
                print(" !ERRO! Insira um NUMERO! >:P\n")
                value = int(-1)
            #retorna para o menu
            if value == 0: 
                Grafer.clear()
                break

            #comeca criacao de grafo denso
            elif value == 1: 
                while True: #Segundo loop do usuario
                    size = input(": Insira quantos vertices o Grafo Denso deverá ter: .: ")

                    try: #checa se size é inteiro
                        size =int(size)

                        if size >= 0: #checa se é numero natural
                            #cria o grafo e da append na lista de grafos geral
                            listaDeGrafos.append(Grafer.criarGrafoDenso(size))

                            Grafer.clear()
                            print(": Grafo Denso criado!")
                            print(": Confira ele no menu de grafos ja criados!\n")
                            break

                        else:
                            Grafer.clear()
                            print(" !ERRO! Insira um numero MAIOR QUE ZERO! >:P\n")

                    except ValueError:
                        Grafer.clear()
                        print(" !ERRO! Insira um NUMERO INTEIRO! >:P\n")

            #comeca criacao de grafo esparso
            elif value == 2:
                Grafer.criarGrafoEsparso()

            #confere se maior q zero
            elif value < 0:
                Grafer.clear()
                print(" !ERRO! Insira um numero MAIOR QUE ZERO! >:P\n")
    
    #menu para adicionar aresta
    def menuAdicionaAresta(self):
        return super().menuAdicionaAresta()
    
    #menu que se comporta como uma funcao main
    def menuMaster ():

        listaDeGrafos = [[1, 2, 3], 2] #Lista de Grafos deve ser criada em memoria no inico do programa

        while True:
            select = Grafer.menuIntro(listaDeGrafos)        
            if select == 1:
                Grafer.menuGrafosJaCriados(listaDeGrafos)
            elif select == 2:
                Grafer.menuCriaGrafo(listaDeGrafos)
            elif select == 3:
                print()
            elif select == 4:
                print()

    
    #=================================================================#
    #----------------------------------------------------------#
    #Atividade 4:
    def dict(num):
        vertices = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E"
    }
        num2letra = vertices[num]
        return num2letra

    def numero_de_vertices(grafo):
        return print(len(grafo)) #retorna o numero de vertices
    
    def numero_de_arestas(grafo):
        counter = int(0)
        for i in range(len(grafo)):
            for j in range(len(grafo[i])):
                if grafo[i][j] == 1:
                    counter = counter + 1
        counter = counter/2
        return print(int(counter)) #retorna o numero de arestas
    
    def sequencia_de_graus(grafo):
        graus = [1 for _ in range(5)] 
        counter = int(0)
        counter2 = int(0)

        for i in range(len(grafo)):
            for j in range(len(grafo[i])):
                if grafo[i][j] == 1:
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

    def imprimir(grafo):
        for i in range(len(grafo)):
            for j in range(len(grafo[i])):
                print(grafo[i][j] , end=" ")
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
from abc import ABC, abstractmethod

class Grafo (ABC):

    #----------------------------------------#
    #Metodos para criacao de grafos e melhor usabilidade
    #do programa

    @abstractmethod
    def criarGrafoDenso(size):
        pass

    @abstractmethod
    def criarGrafoEsparso(self):
        pass

    @abstractmethod
    def menuGrafosJaCriados(self):
        pass

    @abstractmethod
    def menuCriaGrafo(self):
        pass

    @abstractmethod
    def menuAdicionaAresta(self):
        pass

    @abstractmethod
    def menuFuctionsEntreGrafos(self):
        pass

    @abstractmethod
    def menuIntro(self):
        pass 

    @abstractmethod
    def menuMaster(self):
        pass    

    #----------------------------------------#
    #Atividade 4:
    @abstractmethod
    def dictionary(self):
        pass

    @abstractmethod
    def numero_de_vertices(self):
        pass

    @abstractmethod
    def numero_de_arestas(self):
        pass

    @abstractmethod
    def sequencia_de_grafos(self):
        pass

    @abstractmethod
    def sequencia_de_graus(self):
        pass

    @abstractmethod
    def adicionar_aresta(self, u, v):
        pass

    @abstractmethod
    def remover_aresta(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass
    #--------------------------------------#
    #Atividade 5:
    @abstractmethod
    def is_simples(self):
        pass

    @abstractmethod
    def is_nulo(self):
        pass

    @abstractmethod
    def is_completo(self):
        pass
    #--------------------------------------#
    #Atividade 6:

    @abstractmethod
    def get_vertices(self):
        pass

    @abstractmethod
    def get_arestas(self):
        pass

    @abstractmethod
    def is_subgrafo(subGrafo, grafo):
        pass

    @abstractmethod
    def is_subgrafo_gerador(self):
        pass

    @abstractmethod
    def is_subgrafo_induzido(self):
        pass

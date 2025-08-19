from grafoInterface import Grafo

class Grafer(Grafo):
    
    def __init__(self, vertices):  # construtor
        alfabeto = vertices.split()

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

        return print(f"Aresta adicionada entre {u} e {v}.")

    def remover_aresta(grafo, u, v):

        grafo[u][v] = 0
        grafo[v][u] = 0

        return print(f"Aresta removida entre {u} e {v}.")
    
    def sequencia_de_grafos():
        return print("")

    def imprimir(grafo):
        for i in range(len(grafo)):
            for j in range(len(grafo[i])):
                print(grafo[i][j] , end=" ")
            print("")
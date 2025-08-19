from grafo import Grafer

def main():

    A = 0
    B = 1
    C = 2
    D = 3
    E = 4

    sizeGrafo = int(5)
    grafo = [[0 for _ in range(sizeGrafo)] for _ in range(sizeGrafo)]

    Grafer.adicionar_aresta(grafo, A, B)
    Grafer.adicionar_aresta(grafo, A, C)
    Grafer.adicionar_aresta(grafo, C, C)
    Grafer.adicionar_aresta(grafo, C, E)
    Grafer.adicionar_aresta(grafo, B, D)
    
    Grafer.imprimir(grafo)
    Grafer.numero_de_vertices(grafo)
    Grafer.numero_de_arestas(grafo)
    Grafer.sequencia_de_graus(grafo)

    Grafer.remover_aresta(grafo, A, C)

    Grafer.imprimir(grafo)

    

main()

#  A B C D E
#A 1 0 0 0 0 -> 5
#B 1 1 0 0 0 -> 5
#C 1 1 1 1 1 -> 5
#D 1 1 1 1 1 -> 5
#E 1 1 1 1 1 -> 5 = 25/2 =12.5
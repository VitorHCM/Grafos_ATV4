from grafo import Grafer

def main():

    print("-----------------------------------")
    print("Atividade 4 - Matriz de Adjacência")
    print("")

    sizeGrafo = int(5)
    grafo = [[0 for _ in range(sizeGrafo)] for _ in range(sizeGrafo)]
    Grafer.adicionar_aresta(grafo, 0, 1)
    Grafer.adicionar_aresta(grafo, 0, 2)
    Grafer.adicionar_aresta(grafo, 2, 2)
    Grafer.adicionar_aresta(grafo, 2, 4)
    Grafer.adicionar_aresta(grafo, 1, 3)
    
    Grafer.imprimir(grafo)
    Grafer.numero_de_vertices(grafo)
    Grafer.numero_de_arestas(grafo)
    Grafer.sequencia_de_graus(grafo)

    Grafer.remover_aresta(grafo, 0, 2)

    Grafer.imprimir(grafo)

    print("")
    print("-----------------------------------")
    print("Atividade 5 - Grafo Simples - Nulo - Completo")
    print("")

    Grafer.is_simples(grafo)
    Grafer.is_nulo(grafo)
    Grafer.is_completo(grafo)

def main2 ():

    print("")
    print("-----------------------------------")
    print("Atividade 6 - Subgrafos")
    print("")

    grafoEsparso = {}
    subGrafo = {}

    grafoEsparso["A"] = []
    grafoEsparso["B"] = []
    grafoEsparso["C"] = []
    grafoEsparso["D"] = []
    grafoEsparso["E"] = []

    subGrafo["C"] = []
    subGrafo["D"] = []
    subGrafo["E"] = []
    
    print(Grafer.get_vertices(grafoEsparso))
    print(Grafer.get_arestas(grafoEsparso))
    Grafer.is_subgrafo(subGrafo, grafoEsparso)

def main3 ():
    Grafer.menuMaster()
    
#main()

#main2()

main3()
# Criando um grafo vazio
# grafo["A"] = []
# grafo["B"] = []
# print("Vértices:", grafo.keys())
# # Adiciona aresta de A para B
# grafo["A"].append("B")
# grafo["B"].append("A")  # se o grafo for não direcionado
# print("Grafo:", grafo)
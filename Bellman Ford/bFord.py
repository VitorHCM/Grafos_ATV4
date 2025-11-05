#Aluno Vitor Hugo Campos 2312130182

arestas = [
    ('S', 'A', 3),
    ('S', 'B', 5),
    ('S', 'D', 2),
    ('B', 'A', 6),
    ('B', 'C', 8),
    ('B', 'D', -9),
    ('A', 'C', -5),
    ('A', 'D', 8),
    ('C', 'D', -3)
]

# Dict de vértices
vertices = {'S', 'A', 'B', 'C', 'D'}

def bellman_ford(vertices, arestas, start):

    # Preenche o dict dist com inf e os indices com os vertices
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0

    # Relaxa todas as arestas |V| - 1 vezes
    for _ in range(len(vertices) - 1):
        for u, v, w in arestas:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Verifica se há ciclo negativo
    for u, v, w in arestas:
        if dist[u] + w < dist[v]:
            print("O grafo contém ciclo de peso negativo.")
            return None

    return dist

# Executa o algoritmo a partir de S
distancias = bellman_ford(vertices, arestas, 'S')

if distancias:
    print("Distâncias mínimas a partir de S:")
    for v in sorted(distancias):
        print(f"S → {v} = {distancias[v]}")
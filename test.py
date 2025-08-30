
import os

def clear():
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For Linux / Mac
    else:
        os.system("clear")

clear()

grafos = []

g0 = []
g1 = {'a':['b','c'], 'b': ['c'], 'c': ['a']}
g2 = {1: [2, 3], 2: [1], 3: [2]}
G3 = [[0 for _ in range(3)] for _ in range(3)]
for i in range (len(G3)):
    G3[i][i] = 1

print(G3)

for i in range(len(G3)):
            for j in range(len(G3[i])):
                print(G3[i][j] , end=" ")
            print("")

grafos.append(g1)

grafos.append(g2)

grafos.append(G3)
for i in range(len(grafos)):
    print(f"Grafo {i}",grafos[i])

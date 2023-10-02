import Tree
import sys
import time


def getRootAndAlgorithm():
  # Recebendo algoritmo
    algorithm = sys.argv[1]
    if(algorithm not in ["B", "I", "U", "A", "G", "H"]):
        raise ValueError("Algoritmo escolhido inválido")
  
  # Recebendo posicoes do 8-puzzle
    input = [[],[],[]]
    for i in range(9):
        input[i//3].append(int(sys.argv[i+2]))

    initialState = Tree.Node(input)

    return initialState, algorithm

root, algorithm = getRootAndAlgorithm()

solution = None

if(algorithm == "B"):
    inicio = time.time()
    solution = Tree.bfs(root)
    fim = time.time()
    print(fim - inicio)
    print(solution.level[0])
elif(algorithm == "I"):
    inicio = time.time()
    solution = Tree.ids(root)
    fim = time.time()
    print(fim - inicio)
    print(solution.level[0])
elif(algorithm == "U"):
    inicio = time.time()
    solution = Tree.dijkstra(root)
    fim = time.time()
    print(fim - inicio)
    print(solution.level[0])
elif(algorithm == "A"):
    inicio = time.time()
    solution = Tree.AStar(root)
    fim = time.time()
    print(fim - inicio)
    print(solution.level[0])
elif(algorithm == "G"):
    inicio = time.time()
    solution = Tree.greedyBestFirstSearch(root)
    fim = time.time()
    print(fim - inicio)
    print(solution.level[0])
elif(algorithm == "H"):
    inicio = time.time()
    solution = Tree.hillClimbing(root)
    fim = time.time()
    print(fim - inicio)
    print(solution.level[0])
else:
    raise ValueError("Algoritmo escolhido inválido")
  
if(sys.argv[11] == "PRINT"):
    print("")
    solution.printPath()
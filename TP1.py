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
    
    solution = Tree.bfs(root)
    print(solution.level[0])
    
elif(algorithm == "I"):
    
    solution = Tree.ids(root)
    print(solution.level[0])

elif(algorithm == "U"):
    
    solution = Tree.dijkstra(root)
    print(solution.level[0])

elif(algorithm == "A"):
    
    solution = Tree.AStar(root)
    print(solution.level[0])

elif(algorithm == "G"):
    
    solution = Tree.greedyBestFirstSearch(root)
    print(solution.level[0])

elif(algorithm == "H"):
    
    solution = Tree.hillClimbing(root)
    print(solution.level[0])

else:
    raise ValueError("Algoritmo escolhido inválido")
  
if(sys.argv[11] == "PRINT"):
    print("")
    solution.printPath()
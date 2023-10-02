import Tree
import sys


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

if(algorithm == "B"):
    solution = Tree.bfs(root)
    print(solution[0])
elif(algorithm == "I"):
    print(Tree.iterativeDeepening(root))
elif(algorithm == "U"):
    print(Tree.uniformCostSearch(root))
elif(algorithm == "A"):
    print(Tree.aStar(root))
elif(algorithm == "G"):
    print(Tree.greedyBestFirstSearch(root))
elif(algorithm == "H"):
    print(Tree.hillClimbing(root))
else:
    raise ValueError("Algoritmo escolhido inválido")
  
if(sys.argv[11] == "PRINT"):
    print("")
    solution[1].printPath()
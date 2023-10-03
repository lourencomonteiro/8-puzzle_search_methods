import copy
import queue
  
class Node:
    def __init__(self, board, level = 0, parent = None):
        self.board = board
        self.children = []
        self.level = level,
        self.cost = 0
        self.parent = parent
    
    def printBoard(self):
        for i in range(3):
            print("{} {} {}".format(self.board[i][0], self.board[i][1], self.board[i][2]))

    def printPath(self):
        if(self.parent != None):
            self.parent.printPath()
        self.printBoard()
        print("")

    def getEmptyPosition(self):
        for i, sublist in enumerate(self.board):
            if 0 in sublist:
                j = sublist.index(0)
                emptyPosition = [i, j]
                break
        return emptyPosition

    def setCost(self, cost):
        self.cost = cost
    
    def movePieceUp(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1, self)
        if(emptyPosition[0] == 2):
            return None
        movedPiece = self.board[emptyPosition[0] +1][emptyPosition[1]]
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = movedPiece
        newBoard.board[emptyPosition[0] + 1][emptyPosition[1]] = 0
        return newBoard
    
    def movePieceDown(self):
        emptyPosition = self.getEmptyPosition().copy()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1, self)
        if(emptyPosition[0] == 0):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0] -1][emptyPosition[1]]
        newBoard.board[emptyPosition[0] -1][emptyPosition[1]] = 0
        return newBoard
    
    def movePieceLeft(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1, self)
        if(emptyPosition[1] == 2):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] +1]
        newBoard.board[emptyPosition[0]][emptyPosition[1] +1] = 0
        return newBoard
        
    def movePieceRight(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1, self)
        if(emptyPosition[1] == 0):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] -1]
        newBoard.board[emptyPosition[0]][emptyPosition[1] -1] = 0
        return newBoard

    def isSolution(self):
        solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if self.board == solution:
            return True
        return False     

    def generateChildren(self):

        up = self.movePieceUp()
        down = self.movePieceDown()        
        left = self.movePieceLeft()        
        right = self.movePieceRight()
        
        moves = [up, down, left, right]

        for move in moves:
            if(move):
                self.children.append(move)

def bfs(root):
    notVisited = [root]
    solutionNode = None
    while solutionNode == None:
        for node in notVisited:
            if node.isSolution():
                solutionNode = node
                break

        aux = []
        for node in notVisited:
            node.generateChildren()
            for child in node.children:
                aux.append(child)
        notVisited.clear()
        notVisited = aux.copy()
    return solutionNode

def dijkstra(root):
    priorityQueue = queue.Queue()
    priorityQueue.put(root)
    visited = []
    solutionNode = None
    while priorityQueue.empty() == False:
        #seleciona o primeiro item da pilha e remove ele
        node = priorityQueue.get()
        if node.isSolution():
            solutionNode = node
            break
        else:
            visited.append(node)
            node.generateChildren()
            for child in node.children:
                if(child not in visited): priorityQueue.put(child)
    
    if(solutionNode == None):
        return False
    return solutionNode

def ids(root):
    depthLimit = 0
    while (1):  # Loop até encontrar o objetivo ou explorar toda a árvore
        solution = dfs(root, depthLimit)
        if(solution != False):
            return solution
        depthLimit = depthLimit + 1

def dfs(root, depthLimit):
    notVisitedStack = queue.LifoQueue()
    notVisitedStack.put(root)
    solutionNode = None
    while notVisitedStack.empty() == False:
        node = notVisitedStack.get()
        if node.isSolution():
            solutionNode = node
            break
        if node.level[0] < depthLimit:
            node.generateChildren()
            for child in node.children:
                notVisitedStack.put(child)
    if(solutionNode != None):
        return solutionNode
    return False

def numberOfPiecesInWrongPlace(node):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    wrongPlace = 0
    for i in range(3):
        for j in range(3):
            if node.board[i][j] != solution[i][j]:
                wrongPlace += 1
    return wrongPlace

def AStar(root):
    priorityQueue = [root]
    visited = []
    solutionNode = None
    while len(priorityQueue) != 0:
        #seleciona o primeiro item da pilha e remove ele
        node = priorityQueue[0]
        if node.isSolution():
            solutionNode = node
            break
        else: 
            visited.append(node)
            priorityQueue.pop(0)
            node.generateChildren()
            for child in node.children:
                if(child not in visited):
                    child.setCost(1 + numberOfPiecesInWrongPlace(child))
                    priorityQueue.append(child)
        priorityQueue.sort(key=lambda x: x.cost)
    
    if(solutionNode == None):
        return False
    return solutionNode

def manhattanDistance(node):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distance = 0
    for i in range(3):
        for j in range(3):
            if node.board[i][j] != solution[i][j]:
                for k in range(3):
                    for l in range(3):
                        if node.board[i][j] == solution[k][l]:
                            distance += abs(i-k) + abs(j-l)
    return distance

def greedyBestFirstSearch(root):
    priorityQueue = [root]
    visited = []
    solutionNode = None
    while len(priorityQueue) != 0:
        node = priorityQueue[0]
        if node.isSolution():
            solutionNode = node
            break
        else: 
            visited.append(node)
            priorityQueue.pop(0)
            node.generateChildren()
            for child in node.children:
                if(child not in visited):
                    child.setCost(manhattanDistance(child))
                    priorityQueue.append(child)
        priorityQueue.sort(key=lambda x: x.cost)
    
    if(solutionNode == None):
        return False
    return solutionNode

def hillClimbing(root):
    currentNode = root
    root.setCost(manhattanDistance(root))
    k = 5
    while(True):
        currentNode.generateChildren()
        neighbours = currentNode.children
        for node in neighbours:
            node.setCost(manhattanDistance(node))
        bestNeighbour = min(neighbours, key=lambda node: node.cost)
        if(bestNeighbour.cost > currentNode.cost):
            return currentNode
        elif(bestNeighbour.cost == currentNode.cost):
            k -= 1
        if(k == 0):
            return currentNode
        currentNode = bestNeighbour


# import time

# teste0 = [[2, 1, 3], [4, 5, 6], [7, 8, 0]] # solução = 1

# teste1 = [[1, 5, 2], [0, 4, 3], [7, 8, 6]] # solução = 5
# teste2 = [[5, 8, 2], [1, 0, 3], [4, 7, 6]] # solução = 10
# teste3 = [[8, 7, 0], [5, 4, 2], [1, 6, 3]] # solução = 20

# testes = [teste0, teste1, teste2, teste3]

# cont = 1
# for i in testes:
#     print("------------------------------")
#     print("")
#     print("Teste {}".format(cont))
#     cont += 1
#     root = Node(i)
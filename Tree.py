import copy
import queue
  
class Node:
    def __init__(self, board, level):
        self.board = board
        self.children = []
        self.level = level,
    
    def printBoard(self):
        for i in range(3):
            print("{} {} {}".format(self.board[i][0], self.board[i][1], self.board[i][2]))

    def getEmptyPosition(self):
        for i, sublist in enumerate(self.board):
            if "-" in sublist:
                j = sublist.index("-")
                emptyPosition = [i, j]
        return emptyPosition

    def movePieceUp(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1)
        if(emptyPosition[0] == 2):
            return None
        movedPiece = self.board[emptyPosition[0] +1][emptyPosition[1]]
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = movedPiece
        newBoard.board[emptyPosition[0] + 1][emptyPosition[1]] = "-"
        return newBoard
    
    def movePieceDown(self):
        emptyPosition = self.getEmptyPosition().copy()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1)
        if(emptyPosition[0] == 0):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0] -1][emptyPosition[1]]
        newBoard.board[emptyPosition[0] -1][emptyPosition[1]] = "-"
        return newBoard
    
    def movePieceLeft(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1)
        if(emptyPosition[1] == 2):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] +1]
        newBoard.board[emptyPosition[0]][emptyPosition[1] +1] = "-"
        return newBoard
        
    def movePieceRight(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board), self.level[0]+1)
        if(emptyPosition[1] == 0):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] -1]
        newBoard.board[emptyPosition[0]][emptyPosition[1] -1] = "-"
        return newBoard

    def isSolution(self):
        solution = [[1, 2, 3], [4, 5, 6], [7, 8, "-"]]
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
    solutionLevel = -1
    while solutionLevel == -1:
        for node in notVisited:
            if node.isSolution():
                solutionLevel = node.level
                break

        aux = []
        for node in notVisited:
            node.generateChildren()
            for child in node.children:
                aux.append(child)
        notVisited.clear()
        notVisited = aux.copy()
    return solutionLevel[0]

def dijkstra(root):
    priorityQueue = queue.Queue()
    priorityQueue.put(root)
    visited = []
    solutionLevel = -1
    while solutionLevel == -1:
        if(priorityQueue.empty()):
            return -1
        #seleciona o primeiro item da pilha e remove ele
        node = priorityQueue.get() 
        if node.isSolution():
            solutionLevel = node.level
        else: 
            visited.append(node)
            node.generateChildren()
            for child in node.children:
                if(child not in visited): priorityQueue.put(child)
    
    return solutionLevel[0]

def ids(raiz):
    depthLimit = 0
    while (1):  # Loop até encontrar o objetivo ou explorar toda a árvore
        solutionDepth = dfs(root, depthLimit)
        if(solutionDepth):
            return solutionDepth
        depthLimit = depthLimit + 1

def dfs(root, depthLimit):
    stack = queue.LifoQueue()



    



initialState = [[1, "-", 3], [4, 2, 5], [7, 8, 6]]
root = Node(initialState, 0)
print(bfs(root))
print(dijkstra(root))
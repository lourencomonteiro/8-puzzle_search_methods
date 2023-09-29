import copy
  
class Node:
    def __init__(self, board):
        self.board = board
        self.children = []
    
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
        newBoard = Node(copy.deepcopy(self.board))
        if(emptyPosition[0] == 2):
            return None
        movedPiece = self.board[emptyPosition[0] +1][emptyPosition[1]]
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = movedPiece
        newBoard.board[emptyPosition[0] + 1][emptyPosition[1]] = "-"
        return newBoard
    
    def movePieceDown(self):
        emptyPosition = self.getEmptyPosition().copy()
        newBoard = Node(copy.deepcopy(self.board))
        if(emptyPosition[0] == 0):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0] -1][emptyPosition[1]]
        newBoard.board[emptyPosition[0] -1][emptyPosition[1]] = "-"
        return newBoard
    
    def movePieceLeft(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board))
        if(emptyPosition[1] == 2):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] +1]
        newBoard.board[emptyPosition[0]][emptyPosition[1] +1] = "-"
        return newBoard
        
    def movePieceRight(self):
        emptyPosition = self.getEmptyPosition()
        newBoard = Node(copy.deepcopy(self.board))
        if(emptyPosition[1] == 0):
            return None
        newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] -1]
        newBoard.board[emptyPosition[0]][emptyPosition[1] -1] = "-"
        return newBoard

    def isSolution(self):
        for i in range(8):
            nextIndex = i+1
            firstPiece = self.board[i//3][i%3]
            secondPiece = self.board[(nextIndex)//3][(nextIndex)%3]
            if(secondPiece == "-" and self.getEmptyPosition() != [2, 2]): secondPiece = self.board[(nextIndex+1)//3][(nextIndex+1)%3]
            if(type(firstPiece) == int and type(secondPiece) == int and firstPiece > secondPiece):
                return False
        return True     

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
    solutionFound = False
    solutionDepth = 0
    while not solutionFound:
        for node in notVisited:
            if node.isSolution():
                solutionFound = True
                break

        aux = copy.deepcopy(notVisited)
        for node in aux:
            node.generateChildren()
            for child in node.children:
                notVisited.append(child)
            notVisited.pop(0)
        
        solutionDepth +=1
    return solutionDepth



initialState = [[1, 5, 2], ["-", 4, 3], [7, 8, 6]]
root = Node(initialState)
print(bfs(root))
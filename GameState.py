import copy

NUMBER_OF_POSITIONS = 9
NUMBER_OF_LINES = 3
  
class GameState:
  def __init__(self, board):
    self.board = board      

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
    newBoard = GameState(copy.deepcopy(self.board))
    if(emptyPosition[1] == 2):
        return None
    movedPiece = self.board[emptyPosition[0] +1][emptyPosition[1]]
    newBoard.board[emptyPosition[0]][emptyPosition[1]] = movedPiece
    newBoard.board[emptyPosition[0] + 1][emptyPosition[1]] = "-"
    return newBoard
  
  def movePieceDown(self):
    emptyPosition = self.getEmptyPosition().copy()
    newBoard = GameState(copy.deepcopy(self.board))
    if(emptyPosition[0] == 0):
        return None
    newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0] -1][emptyPosition[1]]
    newBoard.board[emptyPosition[0] -1][emptyPosition[1]] = "-"
    return newBoard
  
  def movePieceLeft(self):
    emptyPosition = self.getEmptyPosition()
    newBoard = GameState(copy.deepcopy(self.board))
    if(emptyPosition[1] == 2):
        return None
    newBoard.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] +1]
    newBoard.board[emptyPosition[0]][emptyPosition[1] +1] = "-"
    return newBoard
       
  def movePieceRight(self):
    emptyPosition = self.getEmptyPosition()
    newBoard = GameState(copy.deepcopy(self.board))
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
      if(secondPiece == "-"): secondPiece = self.board[(nextIndex+1)//3][(nextIndex+1)%3]
      if(type(firstPiece) == int and type(secondPiece) == int and firstPiece > secondPiece):
          return False
    return True     


# x = GameState([[2, 1, 3], [4, "-", 5], [6, 7, 8]])
# x.printBoard()
# y = x.movePieceDown()
# y.printBoard()



# receiveInput()
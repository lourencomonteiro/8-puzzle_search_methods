NUMBER_OF_POSITIONS = 9
NUMBER_OF_LINES = 3
  
class State:
  def __init__(self, board):
    self.board = board
    for i, sublist in enumerate(board):
      if "-" in sublist:
        j = sublist.index("-")
        self.emptyPosition = [i, j]
      

  def printBoard(self):
    for i in range(3):
      print("{} {} {}".format(self.board[i][0], self.board[i][1], self.board[i][2]))

  def getEmptyPosition(self):
    return self.emptyPosition

  def movePieceUp(self):
    emptyPosition = self.getEmptyPosition()
    if(emptyPosition[1] == 2):
        return None
    self.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0] +1][emptyPosition[1]]
    self.board[emptyPosition[0] + 1][emptyPosition[1]] = "-"
    self.emptyPosition = [emptyPosition[0] + 1, emptyPosition[1]]
  
  def movePieceDown(self):
    emptyPosition = self.getEmptyPosition()
    if(emptyPosition[0] == 0):
        return None
    self.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0] -1][emptyPosition[1]]
    self.board[emptyPosition[0] -1][emptyPosition[1]] = "-"
    self.emptyPosition = [emptyPosition[0] -1, emptyPosition[1]]
  
  def movePieceLeft(self):
    emptyPosition = self.getEmptyPosition()
    if(emptyPosition[1] == 2):
        return None
    self.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] +1]
    self.board[emptyPosition[0]][emptyPosition[1] +1] = "-"
    self.emptyPosition = [emptyPosition[0], emptyPosition[1] +1]
       
  def movePieceRight(self):
    emptyPosition = self.getEmptyPosition()
    if(emptyPosition[1] == 0):
        return None
    self.board[emptyPosition[0]][emptyPosition[1]] = self.board[emptyPosition[0]][emptyPosition[1] -1]
    self.board[emptyPosition[0]][emptyPosition[1] -1] = "-"
    self.emptyPosition = [emptyPosition[0], emptyPosition[1] -1]

  def isSolution(self):
    for i in range(8):
      nextIndex = i+1
      firstPiece = self.board[i//3][i%3]
      secondPiece = self.board[(nextIndex)//3][(nextIndex)%3]
      if(secondPiece == "-"): secondPiece = self.board[(nextIndex+1)//3][(nextIndex+1)%3]
      if(type(firstPiece) == int and type(secondPiece) == int and firstPiece > secondPiece):
          return False
    return True     

# x = State([[2, 1, 3], [4, "-", 5], [6, 7, 8]])




# receiveInput()
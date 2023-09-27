import sys
import GameState as gs

NUMBER_OF_POSITIONS = 9
NUMBER_OF_LINES = 3

def receiveInput():
  # Recebendo algoritmo
  algorithm = sys.argv[1]
  if(algorithm not in ["B", "I", "U", "A", "G", "H"]):
    raise ValueError("Algoritmo escolhido inválido")
  
  # Recebendo posicoes do 8-puzzle
  input = [[],[],[]]
  for i in range(9):
      if(sys.argv[i] == 0): input[i//3].append("-") 
      else: input[i//3].append(sys.argv[i+2])

  initialState = gs.GameState(input)
  if(sys.argv[11] == "PRINT"):
     initialState.printBoard()

  return initialState

initialState = receiveInput()

print(initialState.isSolution())
  
import sys

NUMBER_OF_POSITIONS = 9
NUMBER_OF_LINES = 3

def receiveInput():
  # Recebendo algoritmo
  algorithm = sys.argv[1]
  if(algorithm not in ["B", "I", "U", "A", "G", "H"]):
    raise ValueError("Algoritmo escolhido inválido")
  
  # Recebendo posicoes do 8-puzzle
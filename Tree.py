import GameState as gs
class Node:
    def __init__(self, state):
        self.state = gs.GameState(state)
        self.children = []

    def generateChildren(self):

        up = self.state.movePieceUp()
        down = self.state.movePieceDown()        
        left = self.state.movePieceLeft()        
        right = self.state.movePieceRight()

        moves = [up, down, left, right]

        for move in moves:
            if(move):
                self.children.append(move)



initialState = [[1, 2, 3], [4, "-", 5], [6, 7, 8]]
root = Node(initialState)
# root.state.printBoard()
root.generateChildren()



# for child in root.children:
#     print("Board: ")
#     child.printBoard()







# def bfs(visited, graph, node): #function for BFS
#   visited.append(node)
#   queue.append(node)

#   while queue:          # Creating loop to visit each node
#     m = queue.pop(0) 
#     print (m, end = " ") 

#     for neighbour in graph[m]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)
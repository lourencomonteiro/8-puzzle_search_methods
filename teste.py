class Amigo:
    def __init__(self, nome):
        self.nome = [nome, nome, nome]

a = Amigo("Carlos")
b = Amigo("Felipe")
c = Amigo("Ramon")


arr = [a, b, c]

for i in arr:
    print(i.nome)
class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.neighbors = [] #lista de vizinhos
        self.marked = False

    def setNeighbor(self, id): #setando o vizinho
        self.neighbors.append(id)

    def getNeighbors(self): #pegando a lista de vizinhos
        return self.neighbors

    def getId(self): #pegando o id do vertice
        return self.id

    #vertice pode ser marcado ou não
    def setMarked(self):
        self.marked = True

    def getMarked(self):
        return self.marked
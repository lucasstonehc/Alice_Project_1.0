

class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def setNeighbor(self, id):
        self.neighbors.append(id)

    def getNeighbors(self):
        return self.neighbors

    def getId(self):
        return self.id


class Edge(object):

    def __init__(self,id, vertice_x, vertice_y, weight):
        self.id = id
        self.vertice_x = vertice_x
        self.vertice_y = vertice_y
        self.weight = weight


    def getId(self):
        return self.id

    def getVerticeX(self):
        return self.vertice_x

    def getVerticeY(self):
        return self.vertice_y

    def getWeight(self):
        return self.weight


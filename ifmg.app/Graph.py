from Edge import Edge
from Vertex import Vertex
from GeneratorFile import  GeneratorFile

class Graph(object):
    def __init__(self):
        self.vertices = [] #lista de vertices
        self.edges = [] #lista de arestas
        self.generator_file = GeneratorFile()
        self.fill_vertices()
        self.fill_edges()


    def create_vertex(self):
        for i in range(self.generator_file.size_of_matrix()):
            self.vertices.append(Vertex(i)) #vertices criados e adicionados

    def add_neighbors(self):
        matrix = self.generator_file.getMatrix()
        size = self.generator_file.size_of_matrix()

        for row in range(size):
            for column in range(size):
                if matrix[row][column] != '0': #existe ligacao entre os vertices
                    self.vertices[row].setNeighbor(column) #pega o vertice na lista e seta seu vizinho

    def fill_vertices(self):
        self.create_vertex()
        self.add_neighbors()


    def fill_edges(self):

        matrix = self.generator_file.getMatrix()
        size = self.generator_file.size_of_matrix()

        for row in range(size):
            for column in range(size):
                if matrix[row][column] != '0':  # existe ligacao entre os vertices
                    weight = matrix[row][column]
                    self.edges.append(Edge(row,row,column,weight))


    def getVertices(self):
        return self.vertices

    def getEdges(self):
        return self.edges

    def getEdge(self, vertice_x, vertice_y):
        edge = None
        for i in range(len(self.edges)):
            if vertice_x  == self.edges[i].getVerticeX() and vertice_y == self.edges[i].getVerticeY():
                edge = self.edges[i]
        return edge
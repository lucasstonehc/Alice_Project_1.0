from Edge import Edge
from Vertex import Vertex

class Graph(object):
    def __init__(self):
        self.vertices = [] #lista de vertices
        self.edges = [] #lista de arestas
        self.fill_vertices()
        #self.fill_edges() busca em profundidade nao precisaremos desta função

    def fill_vertices(self):
        vertex = Vertex(0)
        vertex.setNeighbor(1)
        vertex.setNeighbor(2)
        vertex.setNeighbor(3)
        vertex.setNeighbor(4)
        self.vertices.append(vertex)
        vertex = Vertex(1)
        vertex.setNeighbor(4)
        vertex.setNeighbor(5)
        self.vertices.append(vertex)
        vertex = Vertex(2)
        vertex.setNeighbor(0)
        vertex.setNeighbor(3)
        self.vertices.append(vertex)
        vertex = Vertex(3)
        vertex.setNeighbor(0)
        vertex.setNeighbor(2)
        vertex.setNeighbor(4)
        vertex.setNeighbor(6)
        self.vertices.append(vertex)
        vertex = Vertex(4)
        vertex.setNeighbor(0)
        vertex.setNeighbor(1)
        vertex.setNeighbor(3)
        vertex.setNeighbor(7)
        self.vertices.append(vertex)
        vertex = Vertex(5)
        vertex.setNeighbor(1)
        self.vertices.append(vertex)
        vertex = Vertex(6)
        vertex.setNeighbor(3)
        vertex.setNeighbor(7)
        self.vertices.append(vertex)
        vertex = Vertex(7)
        vertex.setNeighbor(4)
        vertex.setNeighbor(6)
        self.vertices.append(vertex)

    def fill_edges(self):
        edge = Edge(1,1,2,1)
        self.edges.append(edge)
        edge = Edge(2, 1, 3, 3)
        self.edges.append(edge)
        edge = Edge(3, 2, 3, 1)
        self.edges.append(edge)
        edge = Edge(4, 2, 4, 1)
        self.edges.append(edge)
        edge = Edge(5, 2, 5, 4)
        self.edges.append(edge)
        edge = Edge(6, 3, 4, 3)
        self.edges.append(edge)
        edge = Edge(7, 3, 5, 2)
        self.edges.append(edge)
        edge = Edge(8, 4, 5, 2)
        self.edges.append(edge)
        edge = Edge(9, 4, 6, 1)
        self.edges.append(edge)
        edge = Edge(10, 5, 6, 2)
        self.edges.append(edge)

    def getVertices(self):
        return self.vertices

    def getVertex(self, id):
        return self.vertices[id] #retorna o vertice

    def getEdges(self):
        return self.edges

    def getEdge(self, vertice_x, vertice_y):
        edge = None
        for i in range(len(self.edges)):
            if vertice_x  == self.edges[i].getVerticeX() and vertice_y == self.edges[i].getVerticeY():
                edge = self.edges[i]
        return edge